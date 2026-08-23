from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.analytics import AnalyticsResponse

router = APIRouter(prefix="/api/analytics", tags=["analytics"])

@router.get("", response_model=AnalyticsResponse)
async def get_analytics(db: AsyncSession = Depends(get_db)):
    return AnalyticsResponse(
        total_runs=0,
        successful_runs=0,
        failed_runs=0,
        healed_runs=0,
        total_records=0,
        records_recovered=0,
        avg_recovery_time_seconds=0.0,
        run_history=[],
        healing_history=[]
    )
