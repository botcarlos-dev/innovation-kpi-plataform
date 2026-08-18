from decimal import Decimal


def calculate_budget_variance(
    planned_cost: Decimal,
    actual_cost: Decimal,
) -> Decimal:
    if planned_cost == 0:
        raise ValueError("Planned cost cannot be zero.")

    variance = ((actual_cost - planned_cost) / planned_cost) * Decimal("100")

    return variance.quantize(Decimal("0.01"))


def evaluate_kpi_status(
    value: Decimal,
    warning_threshold: Decimal,
    critical_threshold: Decimal,
) -> str:

    if value >= critical_threshold:
        return "CRITICAL"

    if value >= warning_threshold:
        return "WARNING"

    return "HEALTHY"
