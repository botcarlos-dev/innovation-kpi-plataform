from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.financial_record import FinancialRecord
from app.models.project import Project
from app.schemas.financial_record import (
    FinancialRecordCreate,
    FinancialRecordResponse,
)
from app.models.kpi import KPI
from app.services.kpi_measurement_service import create_kpi_measurement

router = APIRouter(
    prefix="/financial-records",
    tags=["Financial Records"],
)


@router.post(
    "/",
    response_model=FinancialRecordResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_financial_record(
    record_data: FinancialRecordCreate,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == record_data.project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    record = FinancialRecord(**record_data.model_dump())

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


@router.get(
    "/",
    response_model=list[FinancialRecordResponse],
)
def get_financial_records(
    db: Session = Depends(get_db),
):
    return db.query(FinancialRecord).all()


@router.post(
    "/{record_id}/calculate-budget-variance",
)
def calculate_budget_variance_for_record(
    record_id: int,
    db: Session = Depends(get_db),
):
    record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Financial record not found",
        )

    kpi = db.query(KPI).filter(KPI.name == "Budget Variance").first()

    if not kpi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Budget Variance KPI not found",
        )

    measurement = create_kpi_measurement(
        db=db,
        project_id=record.project_id,
        kpi=kpi,
        measurement_date=record.record_date,
        input_data={
            "planned_cost": record.planned_cost,
            "actual_cost": record.actual_cost,
        },
    )

    return {
        "kpi": kpi.name,
        "project_id": measurement.project_id,
        "value": float(measurement.value),
        "status": measurement.status,
        "measurement_date": measurement.measurement_date,
    }
