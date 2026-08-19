from decimal import Decimal

import pytest

from app.services.kpi_engine import (
    calculate_budget_variance,
    evaluate_kpi_status,
    calculate_kpi,
)


def test_budget_variance():
    result = calculate_budget_variance(
        Decimal("120000"),
        Decimal("140000"),
    )

    assert result == Decimal("16.67")


def test_budget_variance_healthy():
    result = evaluate_kpi_status(
        Decimal("4.5"),
        Decimal("10"),
        Decimal("15"),
    )

    assert result == "HEALTHY"


def test_budget_variance_warning():
    result = evaluate_kpi_status(
        Decimal("12"),
        Decimal("10"),
        Decimal("15"),
    )

    assert result == "WARNING"


def test_budget_variance_critical():
    result = evaluate_kpi_status(
        Decimal("16.67"),
        Decimal("10"),
        Decimal("15"),
    )

    assert result == "CRITICAL"


def test_zero_planned_cost():
    with pytest.raises(ValueError):
        calculate_budget_variance(
            Decimal("0"),
            Decimal("100"),
        )


def test_generic_budget_variance():
    result = calculate_kpi(
        "BUDGET_VARIANCE",
        {
            "planned_cost": Decimal("120000"),
            "actual_cost": Decimal("140000"),
        },
    )

    assert result == Decimal("16.67")


def test_generic_progress():
    result = calculate_kpi(
        "PROGRESS",
        {
            "completed": Decimal("75"),
            "total": Decimal("100"),
        },
    )

    assert result == Decimal("75.00")


def test_generic_roi():
    result = calculate_kpi(
        "ROI",
        {
            "benefit": Decimal("150000"),
            "investment": Decimal("100000"),
        },
    )

    assert result == Decimal("50.00")


def test_generic_forecast_accuracy():
    result = calculate_kpi(
        "FORECAST_ACCURACY",
        {
            "actual": Decimal("100000"),
            "forecast": Decimal("95000"),
        },
    )

    assert result == Decimal("94.74")
