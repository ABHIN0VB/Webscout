import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Text, DateTime, Uuid
from app.database import Base

class ScraperRun(Base):
    __tablename__ = "scraper_runs"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    collector_id = Column(String(100), nullable=False)
    source = Column(String(500), nullable=True)
    status = Column(String(50), nullable=False)
    records = Column(Integer, default=0)
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)
    error = Column(Text, nullable=True)
    snapshot_id = Column(String(200), nullable=True)
