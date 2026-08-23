from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
from uuid import UUID
from datetime import datetime

class ProductSpecifications(BaseModel):
    processor: Optional[str] = None
    ram: Optional[str] = None
    storage: Optional[str] = None
    gpu: Optional[str] = None
    display: Optional[str] = None
    battery: Optional[str] = None

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    model_name: Optional[str] = None
    price: Optional[float] = None
    currency: str = "INR"
    url: Optional[str] = None
    image_url: Optional[str] = None
    availability: Optional[str] = None
    rating: Optional[float] = None
    specifications: Optional[dict[str, Any]] = None
    source: Optional[str] = None
    scraped_at: Optional[datetime] = None

    model_config = ConfigDict(protected_namespaces=())

class ProductCreate(ProductBase):
    content_hash: Optional[str] = None
    raw_data: Optional[dict[str, Any]] = None

class ProductResponse(ProductBase):
    id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class ProductBrief(BaseModel):
    id: UUID
    name: str
    brand: Optional[str] = None
    price: Optional[float] = None
    currency: str = "INR"
    image_url: Optional[str] = None
    rating: Optional[float] = None
    key_specs: Optional[str] = None
    source: Optional[str] = None

class ProductCompareRequest(BaseModel):
    product_ids: list[UUID]

class ProductCompareResponse(BaseModel):
    products: list[ProductResponse]
    comparison: dict[str, Any]
