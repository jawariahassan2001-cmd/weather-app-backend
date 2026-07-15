from pydantic import BaseModel, field_validator
from typing import Optional, Any
from datetime import datetime


class SearchCreate(BaseModel):
    location_query: str

    @field_validator("location_query")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("location_query cannot be empty")
        return v.strip()


class SearchUpdate(BaseModel):
    location_query: Optional[str] = None


class SearchResponse(BaseModel):
    id: int
    location_query: str
    resolved_location: Optional[str]
    weather_data: Any
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True