from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.kpi_alert import KPIAlert
from app.schemas.kpi_alert import (
    KPIAlertAcknowledge,
    KPIAlertResponse,
)


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get(
    "/",
    response_model=list[KPIAlertResponse],
)
def get_alerts(
    db: Session = Depends(get_db),
):
    return db.query(KPIAlert).order_by(KPIAlert.created_at.desc()).all()


@router.get(
    "/critical",
    response_model=list[KPIAlertResponse],
)
def get_critical_alerts(
    db: Session = Depends(get_db),
):
    return (
        db.query(KPIAlert)
        .filter(
            KPIAlert.severity == "CRITICAL",
            KPIAlert.acknowledged == False,
        )
        .order_by(KPIAlert.created_at.desc())
        .all()
    )


@router.patch(
    "/{alert_id}/acknowledge",
    response_model=KPIAlertResponse,
)
def acknowledge_alert(
    alert_id: int,
    data: KPIAlertAcknowledge,
    db: Session = Depends(get_db),
):
    alert = db.query(KPIAlert).filter(KPIAlert.id == alert_id).first()

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    alert.acknowledged = data.acknowledged

    db.commit()
    db.refresh(alert)

    return alert
