from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class ScraperStatus(BaseModel):
    collector_id: str
    status: str
    last_run: Optional[datetime] = None
    records: int = 0
    target_url: Optional[str] = None

class ScraperRunResponse(BaseModel):
    id: UUID
    collector_id: str
    source: Optional[str] = None
    status: str
    records: int
    started_at: datetime
    completed_at: Optional[datetime] = None
    error: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)

class HealingEventResponse(BaseModel):
    id: UUID
    collector_id: str
    description: str
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    command_output: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)

class PipelineStep(BaseModel):
    name: str
    status: str
    detail: Optional[str] = None

class PipelineStatus(BaseModel):
    steps: list[PipelineStep]
