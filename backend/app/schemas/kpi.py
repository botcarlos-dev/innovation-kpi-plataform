from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class KPIBase(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=150,
    )

    description: str

    category: str = Field(
        min_length=2,
        max_length=100,
    )

    unit: str = Field(
        min_length=1,
        max_length=30,
    )

    target_value: Decimal
    warning_threshold: Decimal
    critical_threshold: Decimal

    formula: str


class KPICreate(KPIBase):
    pass


class KPIResponse(KPIBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
