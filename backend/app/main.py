from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.projects import router as projects_router
from app.database import get_db
from app.api.kpis import router as kpis_router
from app.api.financial_records import router as financial_records_router
from app.api.kpi_measurements import router as kpi_measurements_router

app = FastAPI(
    title="Innovation KPI Intelligence Platform",
    version="0.1.0",
)

app.include_router(projects_router)
app.include_router(kpis_router)
app.include_router(financial_records_router)
app.include_router(kpi_measurements_router)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
        "service": "innovation-kpi-api",
    }
