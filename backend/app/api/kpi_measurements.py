from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.kpi_measurement import KPIMeasurement


router = APIRouter(
    prefix="/kpi-measurements",
    tags=["KPI Measurements"],
)


@router.get("/")
def get_measurements(
    db: Session = Depends(get_db),
):
    return db.query(KPIMeasurement).order_by(KPIMeasurement.measurement_date).all()
