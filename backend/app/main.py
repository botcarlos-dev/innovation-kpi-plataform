from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.projects import router as projects_router
from app.database import get_db

app = FastAPI(
    title="Innovation KPI Intelligence Platform",
    version="0.1.0",
)

app.include_router(projects_router)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
        "service": "innovation-kpi-api",
    }
