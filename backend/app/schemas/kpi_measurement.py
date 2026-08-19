from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class KPIMeasurementCreate(BaseModel):
    project_id: int
    kpi_id: int
    measurement_date: date
    input_data: dict[str, Decimal]


class KPIMeasurementResponse(BaseModel):
    id: int
    project_id: int
    kpi_id: int
    value: Decimal
    measurement_date: date
    status: str
    input_data: dict

    model_config = ConfigDict(from_attributes=True)
