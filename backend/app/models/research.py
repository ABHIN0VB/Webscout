import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, Integer, Float, JSON, DateTime, ForeignKey, Uuid
from sqlalchemy.orm import relationship
from app.database import Base

class Research(Base):
    __tablename__ = "researches"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    query = Column(Text, nullable=False)
    parsed_requirements = Column(JSON, nullable=True)
    status = Column(String(50), default="pending")
    product_count = Column(Integer, default=0)
    relevant_count = Column(Integer, default=0)
    top_match_count = Column(Integer, default=0)
    recommendation = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)

    results = relationship("ResearchResult", back_populates="research", cascade="all, delete-orphan")

class ResearchResult(Base):
    __tablename__ = "research_results"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    research_id = Column(Uuid, ForeignKey("researches.id"), nullable=False)
    product_id = Column(Uuid, ForeignKey("products.id"), nullable=False)
    score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)
    reasoning = Column(Text, nullable=True)
    score_breakdown = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    research = relationship("Research", back_populates="results")
    product = relationship("Product")
