from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class ProjectBase(BaseModel):
    name: str = Field(min_length=3, max_length=150)
    description: str | None = None
    category: str = Field(min_length=2, max_length=100)
    status: str = "PLANNING"

    start_date: date
    target_end_date: date
    actual_end_date: date | None = None

    budget: float = Field(gt=0)


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=150)
    description: str | None = None
    category: str | None = Field(default=None, min_length=2, max_length=100)
    status: str | None = None

    start_date: date | None = None
    target_end_date: date | None = None
    actual_end_date: date | None = None

    budget: float | None = Field(default=None, gt=0)


class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
