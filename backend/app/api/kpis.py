from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.kpi import KPI
from app.schemas.kpi import KPICreate, KPIResponse


router = APIRouter(
    prefix="/kpis",
    tags=["KPIs"],
)


@router.post(
    "/",
    response_model=KPIResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_kpi(
    kpi_data: KPICreate,
    db: Session = Depends(get_db),
):
    existing_kpi = db.query(KPI).filter(KPI.name == kpi_data.name).first()

    if existing_kpi:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="KPI already exists",
        )

    kpi = KPI(**kpi_data.model_dump())

    db.add(kpi)
    db.commit()
    db.refresh(kpi)

    return kpi


@router.get(
    "/",
    response_model=list[KPIResponse],
)
def get_kpis(
    db: Session = Depends(get_db),
):
    return db.query(KPI).all()
