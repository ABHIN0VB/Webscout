from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.scraper_run import ScraperRun
from app.models.healing_event import HealingEvent
from app.schemas.scraper import ScraperRunResponse, HealingEventResponse, ScraperStatus
from app.services.brightdata_service import BrightDataService

router = APIRouter(prefix="/api/scraper", tags=["scraper"])
bd_service = BrightDataService()

@router.get("/status", response_model=ScraperStatus)
async def get_status():
    cid = bd_service.settings.BRIGHTDATA_COLLECTOR_ID
    if not cid:
        return ScraperStatus(collector_id="N/A", status="unknown")
    st = await bd_service.get_collector_status(cid)
    return ScraperStatus(
        collector_id=cid,
        status="healthy" if st.get("status") == "active" else "unknown",
        target_url=bd_service.settings.BRIGHTDATA_TARGET_URL
    )

@router.get("/runs", response_model=list[ScraperRunResponse])
async def get_runs(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(ScraperRun).order_by(ScraperRun.started_at.desc()).limit(50))
    return [ScraperRunResponse.model_validate(r) for r in res.scalars().all()]

@router.get("/healing-events", response_model=list[HealingEventResponse])
async def get_healing_events(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(HealingEvent).order_by(HealingEvent.started_at.desc()).limit(50))
    return [HealingEventResponse.model_validate(r) for r in res.scalars().all()]
