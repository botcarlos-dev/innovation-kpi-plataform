from datetime import date
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.financial_record import FinancialRecord
from app.models.kpi import KPI
from app.models.kpi_measurement import KPIMeasurement
from app.services.kpi_engine import (
    calculate_budget_variance,
    evaluate_kpi_status,
)


def calculate_budget_variance_measurement(
    db: Session,
    financial_record: FinancialRecord,
    kpi: KPI,
) -> KPIMeasurement:

    value = calculate_budget_variance(
        financial_record.planned_cost,
        financial_record.actual_cost,
    )

    status = evaluate_kpi_status(
        value,
        kpi.warning_threshold,
        kpi.critical_threshold,
    )

    measurement = KPIMeasurement(
        project_id=financial_record.project_id,
        kpi_id=kpi.id,
        value=value,
        measurement_date=financial_record.record_date,
        status=status,
    )

    db.add(measurement)
    db.commit()
    db.refresh(measurement)

    return measurement
