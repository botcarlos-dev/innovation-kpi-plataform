from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.models.kpi_alert import KPIAlert
from app.models.kpi_measurement import KPIMeasurement


def create_alert_for_measurement(
    db: Session,
    measurement: KPIMeasurement,
    kpi: KPI,
) -> KPIAlert | None:

    if measurement.status == "HEALTHY":
        return None

    existing_alert = (
        db.query(KPIAlert).filter(KPIAlert.measurement_id == measurement.id).first()
    )

    if existing_alert:
        return existing_alert

    severity = measurement.status

    title = f"{kpi.name} - {severity}"

    message = (
        f"KPI '{kpi.name}' for project "
        f"{measurement.project_id} has reached "
        f"{severity} status with a value of "
        f"{measurement.value} {kpi.unit}."
    )

    alert = KPIAlert(
        project_id=measurement.project_id,
        kpi_id=measurement.kpi_id,
        measurement_id=measurement.id,
        severity=severity,
        title=title,
        message=message,
        acknowledged=False,
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert
