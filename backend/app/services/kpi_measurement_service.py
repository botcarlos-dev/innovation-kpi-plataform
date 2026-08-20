from datetime import date
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.models.kpi_measurement import KPIMeasurement
from app.services.kpi_engine import (
    calculate_kpi,
    evaluate_kpi_status,
)

from app.services.kpi_alert_service import create_alert_for_measurement


def create_kpi_measurement(
    db: Session,
    project_id: int,
    kpi: KPI,
    measurement_date: date,
    input_data: dict[str, Decimal],
) -> KPIMeasurement:

    value = calculate_kpi(
        kpi.formula_type,
        input_data,
    )

    status = evaluate_kpi_status(
        value,
        kpi.warning_threshold,
        kpi.critical_threshold,
        kpi.higher_is_better,
    )

    measurement = KPIMeasurement(
        project_id=project_id,
        kpi_id=kpi.id,
        value=value,
        measurement_date=measurement_date,
        status=status,
        input_data={key: str(value) for key, value in input_data.items()},
    )

    db.add(measurement)
    db.commit()
    db.refresh(measurement)

    create_alert_for_measurement(
        db=db,
        measurement=measurement,
        kpi=kpi,
    )

    return measurement
