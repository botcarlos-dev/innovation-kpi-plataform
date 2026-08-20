from datetime import datetime

from pydantic import BaseModel, ConfigDict


class KPIAlertResponse(BaseModel):
    id: int
    project_id: int
    kpi_id: int
    measurement_id: int
    severity: str
    title: str
    message: str
    acknowledged: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class KPIAlertAcknowledge(BaseModel):
    acknowledged: bool = True
