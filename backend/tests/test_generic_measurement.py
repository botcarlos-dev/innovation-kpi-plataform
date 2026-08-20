from decimal import Decimal

from app.services.kpi_engine import calculate_kpi, evaluate_kpi_status


def test_budget_variance_healthy():
    result = evaluate_kpi_status(
        Decimal("4.5"),
        Decimal("10"),
        Decimal("15"),
        higher_is_better=False,
    )
    assert result == "HEALTHY"


def test_budget_variance_warning():
    result = evaluate_kpi_status(
        Decimal("12"),
        Decimal("10"),
        Decimal("15"),
        higher_is_better=False,
    )
    assert result == "WARNING"


def test_budget_variance_critical():
    result = evaluate_kpi_status(
        Decimal("16.67"),
        Decimal("10"),
        Decimal("15"),
        higher_is_better=False,
    )
    assert result == "CRITICAL"


def test_budget_variance():
    result = calculate_kpi(
        "BUDGET_VARIANCE",
        {
            "planned_cost": Decimal("100000"),
            "actual_cost": Decimal("112400"),
        },
    )

    assert result == Decimal("12.40")


def test_progress():
    result = calculate_kpi(
        "PROGRESS",
        {
            "completed": Decimal("75"),
            "total": Decimal("100"),
        },
    )

    assert result == Decimal("75.00")


def test_roi():
    result = calculate_kpi(
        "ROI",
        {
            "benefit": Decimal("150000"),
            "investment": Decimal("100000"),
        },
    )

    assert result == Decimal("50.00")


def test_forecast_accuracy():
    result = calculate_kpi(
        "FORECAST_ACCURACY",
        {
            "actual": Decimal("100000"),
            "forecast": Decimal("95000"),
        },
    )

    assert result == Decimal("94.74")
