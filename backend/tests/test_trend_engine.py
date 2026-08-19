from decimal import Decimal

from app.services.trend_engine import (
    calculate_change,
    count_consecutive_increases,
    determine_trend,
)


def test_change():
    result = calculate_change(
        Decimal("16.67"),
        Decimal("12.40"),
    )

    assert result == Decimal("4.27")


def test_budget_variance_worsening():
    values = [
        Decimal("3.20"),
        Decimal("4.80"),
        Decimal("6.10"),
        Decimal("8.90"),
        Decimal("12.40"),
        Decimal("16.67"),
    ]

    result = determine_trend(
        values,
        higher_is_better=False,
    )

    assert result == "WORSENING"


def test_progress_improving():
    values = [
        Decimal("20"),
        Decimal("40"),
        Decimal("60"),
        Decimal("80"),
    ]

    result = determine_trend(
        values,
        higher_is_better=True,
    )

    assert result == "IMPROVING"


def test_stable():
    values = [
        Decimal("20"),
        Decimal("25"),
        Decimal("22"),
        Decimal("27"),
    ]

    result = determine_trend(
        values,
        higher_is_better=True,
    )

    assert result == "STABLE"


def test_consecutive_increases():
    values = [
        Decimal("3.20"),
        Decimal("4.80"),
        Decimal("6.10"),
        Decimal("8.90"),
        Decimal("12.40"),
        Decimal("16.67"),
    ]

    result = count_consecutive_increases(values)

    assert result == 5
