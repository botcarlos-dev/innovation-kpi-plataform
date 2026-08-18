from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id: Mapped[int] = mapped_column(primary_key=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    record_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    planned_cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    actual_cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    forecast_cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now,
    )
