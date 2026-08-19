from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.models.kpi_measurement import KPIMeasurement
from app.services.trend_engine import (
    calculate_change,
    count_consecutive_increases,
    determine_trend,
)


def analyse_kpi_trend(
    db: Session,
    project_id: int,
    kpi_id: int,
):
    measurements = (
        db.query(KPIMeasurement)
        .filter(
            KPIMeasurement.project_id == project_id,
            KPIMeasurement.kpi_id == kpi_id,
        )
        .order_by(KPIMeasurement.measurement_date)
        .all()
    )

    kpi = db.query(KPI).filter(KPI.id == kpi_id).first()

    if not kpi:
        raise ValueError("KPI not found")

    values = [measurement.value for measurement in measurements]

    if len(values) < 2:
        return {
            "trend": "INSUFFICIENT_DATA",
            "measurements": len(values),
        }

    current = values[-1]
    previous = values[-2]

    change = calculate_change(
        current,
        previous,
    )

    trend = determine_trend(
        values,
        kpi.higher_is_better,
    )

    consecutive_increases = count_consecutive_increases(values)

    return {
        "kpi": kpi.name,
        "project_id": project_id,
        "current_value": float(current),
        "previous_value": float(previous),
        "change": float(change),
        "trend": trend,
        "consecutive_increases": (consecutive_increases),
        "measurements": len(values),
    }
