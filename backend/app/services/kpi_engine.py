from decimal import Decimal


def calculate_budget_variance(
    planned_cost: Decimal,
    actual_cost: Decimal,
) -> Decimal:

    if planned_cost == 0:
        raise ValueError("Planned cost cannot be zero.")

    return ((actual_cost - planned_cost) / planned_cost * Decimal("100")).quantize(
        Decimal("0.01")
    )


def calculate_schedule_variance(
    planned_progress: Decimal,
    actual_progress: Decimal,
) -> Decimal:

    if planned_progress == 0:
        raise ValueError("Planned progress cannot be zero.")

    return (
        (actual_progress - planned_progress) / planned_progress * Decimal("100")
    ).quantize(Decimal("0.01"))


def calculate_progress(
    completed: Decimal,
    total: Decimal,
) -> Decimal:

    if total == 0:
        raise ValueError("Total cannot be zero.")

    return (completed / total * Decimal("100")).quantize(Decimal("0.01"))


def calculate_roi(
    benefit: Decimal,
    investment: Decimal,
) -> Decimal:

    if investment == 0:
        raise ValueError("Investment cannot be zero.")

    return ((benefit - investment) / investment * Decimal("100")).quantize(
        Decimal("0.01")
    )


def calculate_forecast_accuracy(
    actual: Decimal,
    forecast: Decimal,
) -> Decimal:

    if forecast == 0:
        raise ValueError("Forecast cannot be zero.")

    error = abs(actual - forecast)

    return (Decimal("100") - (error / forecast * Decimal("100"))).quantize(
        Decimal("0.01")
    )


def evaluate_kpi_status(
    value: Decimal,
    warning_threshold: Decimal,
    critical_threshold: Decimal,
    higher_is_better: bool,
) -> str:
    if higher_is_better:
        if value <= critical_threshold:
            return "CRITICAL"

        if value <= warning_threshold:
            return "WARNING"

        return "HEALTHY"

    if value >= critical_threshold:
        return "CRITICAL"

    if value >= warning_threshold:
        return "WARNING"

    return "HEALTHY"


def calculate_kpi(
    formula_type: str,
    data: dict[str, Decimal],
) -> Decimal:

    if formula_type == "BUDGET_VARIANCE":
        return calculate_budget_variance(
            data["planned_cost"],
            data["actual_cost"],
        )

    if formula_type == "SCHEDULE_VARIANCE":
        return calculate_schedule_variance(
            data["planned_progress"],
            data["actual_progress"],
        )

    if formula_type == "PROGRESS":
        return calculate_progress(
            data["completed"],
            data["total"],
        )

    if formula_type == "ROI":
        return calculate_roi(
            data["benefit"],
            data["investment"],
        )

    if formula_type == "FORECAST_ACCURACY":
        return calculate_forecast_accuracy(
            data["actual"],
            data["forecast"],
        )

    raise ValueError(f"Unknown KPI formula type: {formula_type}")
