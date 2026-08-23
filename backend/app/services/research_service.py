from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from uuid import UUID
from datetime import datetime, timezone
import logging

from app.models.research import Research, ResearchResult
from app.models.product import Product
from app.schemas.research import ResearchResponse, ResearchResultItem
from app.schemas.product import ProductResponse
from app.services.ai_service import AIService
from app.services.brightdata_service import BrightDataService
from app.services.normalization_service import NormalizationService
from app.services.deduplication_service import DeduplicationService
from app.services.ranking_service import RankingService
from app.services.demo_service import DemoService
from app.config import get_settings

logger = logging.getLogger(__name__)


class ResearchService:
    def __init__(self):
        self.ai = AIService()
        self.bd = BrightDataService()
        self.norm = NormalizationService()
        self.dedup = DeduplicationService()
        self.rank = RankingService()
        self.demo = DemoService()
        self.settings = get_settings()

    async def conduct_research(self, query: str, db: AsyncSession) -> ResearchResponse:
        research = Research(query=query, status="pending")
        db.add(research)
        await db.commit()
        await db.refresh(research)

        try:
            reqs = await self.ai.parse_query(query)
            research.parsed_requirements = reqs
            research.status = "collecting"
            await db.commit()

            raw_products = []
            if not self.settings.DEMO_MODE and self.settings.BRIGHTDATA_API_TOKEN:
                try:
                    raw_products = await self.bd.run_collector()
                except Exception as e:
                    logger.warning(f"Bright Data scraping failed ({e}), falling back to demo products...")
                    raw_products = []

            if not raw_products:
                raw_products = self.demo.get_demo_products(query, reqs)

            norm_products = [self.norm.normalize_product(p) for p in raw_products]
            dedup_products = self.dedup.deduplicate(norm_products)

            # Filter by budget ceiling if specified
            budget_max = reqs.get('budget', {}).get('max_price')
            if budget_max and budget_max > 0:
                filtered = [p for p in dedup_products if p.get('price') and p['price'] <= budget_max * 1.20]
                if filtered:
                    dedup_products = filtered

            research.product_count = len(raw_products)
            research.relevant_count = len(dedup_products)
            research.status = "analyzing"
            await db.commit()

            ranked = self.rank.rank_products(dedup_products, reqs)

            db_items = []
            for item in ranked:
                # Extract only valid columns for Product table
                scraped_dt = item.get('scraped_at')
                if isinstance(scraped_dt, str):
                    try:
                        scraped_dt = datetime.fromisoformat(scraped_dt)
                    except ValueError:
                        scraped_dt = None

                prod = Product(
                    name=item.get('name', 'Unknown'),
                    brand=item.get('brand'),
                    model_name=item.get('model_name'),
                    price=item.get('price'),
                    currency=item.get('currency', 'INR'),
                    url=item.get('url'),
                    image_url=item.get('image_url'),
                    availability=item.get('availability', 'In Stock'),
                    rating=item.get('rating'),
                    specifications=item.get('specifications'),
                    source=item.get('source', 'Smartprix'),
                    scraped_at=scraped_dt,
                    content_hash=item.get('content_hash'),
                    raw_data=item.get('raw_data')
                )
                db.add(prod)
                db_items.append((prod, item))

            await db.commit()

            for prod, item in db_items:
                explanation = await self.ai.generate_ranking_explanation(item, reqs, item['score'])
                res = ResearchResult(
                    research_id=research.id,
                    product_id=prod.id,
                    score=item['score'],
                    rank=item['rank'],
                    score_breakdown=item['score_breakdown'],
                    reasoning=explanation
                )
                db.add(res)

            research.top_match_count = len([x for x in ranked if x['score'] > 75])
            research.recommendation = await self.ai.generate_recommendation(ranked, reqs)
            research.status = "completed"
            research.completed_at = datetime.now(timezone.utc)
            await db.commit()

            return await self.get_research(research.id, db)

        except Exception as e:
            logger.error(f"Research failed: {e}", exc_info=True)
            research.status = "failed"
            await db.commit()
            raise

    async def get_research(self, research_id: UUID, db: AsyncSession) -> ResearchResponse:
        stmt = select(Research).options(
            selectinload(Research.results).selectinload(ResearchResult.product)
        ).where(Research.id == research_id)

        result = await db.execute(stmt)
        research = result.scalar_one_or_none()
        if not research:
            return None

        return ResearchResponse(
            id=research.id,
            query=research.query,
            status=research.status,
            parsed_requirements=research.parsed_requirements,
            product_count=research.product_count,
            relevant_count=research.relevant_count,
            top_match_count=research.top_match_count,
            recommendation=research.recommendation,
            created_at=research.created_at,
            completed_at=research.completed_at,
            results=[
                ResearchResultItem(
                    product=ProductResponse.model_validate(r.product),
                    score=r.score,
                    rank=r.rank,
                    reasoning=r.reasoning,
                    score_breakdown=r.score_breakdown
                ) for r in sorted(research.results, key=lambda x: x.rank)
            ]
        )
