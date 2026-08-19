from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.kpi import KPI
from app.models.kpi_measurement import KPIMeasurement
from app.models.project import Project
from app.schemas.kpi_measurement import (
    KPIMeasurementCreate,
    KPIMeasurementResponse,
)
from app.services.kpi_measurement_service import (
    create_kpi_measurement,
)
from app.services.trend_service import (
    analyse_kpi_trend,
)


router = APIRouter(
    prefix="/kpi-measurements",
    tags=["KPI Measurements"],
)


@router.post(
    "/",
    response_model=KPIMeasurementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_measurement(
    measurement_data: KPIMeasurementCreate,
    db: Session = Depends(get_db),
):
    project = (
        db.query(Project).filter(Project.id == measurement_data.project_id).first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    kpi = db.query(KPI).filter(KPI.id == measurement_data.kpi_id).first()

    if not kpi:
        raise HTTPException(
            status_code=404,
            detail="KPI not found",
        )

    measurement = create_kpi_measurement(
        db=db,
        project_id=measurement_data.project_id,
        kpi=kpi,
        measurement_date=(measurement_data.measurement_date),
        input_data=measurement_data.input_data,
    )

    return measurement


@router.get(
    "/",
    response_model=list[KPIMeasurementResponse],
)
def get_measurements(
    db: Session = Depends(get_db),
):
    return db.query(KPIMeasurement).order_by(KPIMeasurement.measurement_date).all()


@router.get("/projects/{project_id}/kpis/{kpi_id}/trend")
def get_kpi_trend(
    project_id: int,
    kpi_id: int,
    db: Session = Depends(get_db),
):
    try:
        return analyse_kpi_trend(
            db,
            project_id,
            kpi_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )
