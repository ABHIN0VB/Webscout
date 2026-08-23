from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Any
from uuid import UUID
from datetime import datetime
from app.schemas.product import ProductResponse

class BudgetConstraint(BaseModel):
    max_price: Optional[float] = None
    min_price: Optional[float] = None
    currency: str = "INR"

class ParsedRequirements(BaseModel):
    category: Optional[str] = None
    budget: Optional[BudgetConstraint] = None
    use_cases: list[str] = Field(default_factory=list)
    preferences: dict[str, Any] = Field(default_factory=dict)

class ResearchRequest(BaseModel):
    query: str

class ResearchResultItem(BaseModel):
    product: ProductResponse
    score: float
    rank: int
    reasoning: Optional[str] = None
    score_breakdown: Optional[dict[str, Any]] = None
    
    model_config = ConfigDict(from_attributes=True)

class ResearchResponse(BaseModel):
    id: UUID
    query: str
    status: str
    parsed_requirements: Optional[dict[str, Any]] = None
    product_count: int
    relevant_count: int
    top_match_count: int
    recommendation: Optional[str] = None
    results: list[ResearchResultItem]
    created_at: datetime
    completed_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
