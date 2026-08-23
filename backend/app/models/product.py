import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, JSON, DateTime, Index, Uuid
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String(500), nullable=False)
    brand = Column(String(200), nullable=True)
    model_name = Column(String(300), nullable=True)
    price = Column(Float, nullable=True)
    currency = Column(String(10), default="INR")
    url = Column(String(2000), nullable=True)
    image_url = Column(String(2000), nullable=True)
    availability = Column(String(100), nullable=True)
    rating = Column(Float, nullable=True)
    specifications = Column(JSON, nullable=True)
    source = Column(String(200), nullable=True)
    scraped_at = Column(DateTime, nullable=True)
    content_hash = Column(String(64), nullable=True, index=True)
    raw_data = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
