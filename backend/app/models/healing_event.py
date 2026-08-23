import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, DateTime, Uuid
from app.database import Base

class HealingEvent(Base):
    __tablename__ = "healing_events"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    collector_id = Column(String(100), nullable=False)
    source = Column(String(500), nullable=True)
    description = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)
    command_output = Column(Text, nullable=True)
