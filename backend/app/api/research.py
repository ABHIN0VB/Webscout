from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.database import get_db
from app.schemas.research import ResearchRequest, ResearchResponse
from app.services.research_service import ResearchService

router = APIRouter(prefix="/api/research", tags=["research"])
research_service = ResearchService()

@router.post("", response_model=ResearchResponse)
async def create_research(request: ResearchRequest, db: AsyncSession = Depends(get_db)):
    return await research_service.conduct_research(request.query, db)

@router.get("/{research_id}", response_model=ResearchResponse)
async def get_research(research_id: UUID, db: AsyncSession = Depends(get_db)):
    res = await research_service.get_research(research_id, db)
    if not res:
        raise HTTPException(status_code=404, detail="Research not found")
    return res
