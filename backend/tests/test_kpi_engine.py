from decimal import Decimal

import pytest

from app.services.kpi_engine import (
    calculate_budget_variance,
    evaluate_kpi_status,
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
