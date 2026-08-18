from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class FinancialRecordCreate(BaseModel):
    project_id: int
    record_date: date

    planned_cost: Decimal = Field(
        ge=0,
    )

    actual_cost: Decimal = Field(
        ge=0,
    )

    forecast_cost: Decimal = Field(
        ge=0,
    )


class FinancialRecordResponse(FinancialRecordCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
