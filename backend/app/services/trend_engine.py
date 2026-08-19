from decimal import Decimal


def calculate_change(
    current: Decimal,
    previous: Decimal,
) -> Decimal:
    return (current - previous).quantize(Decimal("0.01"))


def determine_trend(
    values: list[Decimal],
    higher_is_better: bool,
) -> str:

    if len(values) < 2:
        return "INSUFFICIENT_DATA"

    increasing = all(values[i] > values[i - 1] for i in range(1, len(values)))

    decreasing = all(values[i] < values[i - 1] for i in range(1, len(values)))

    if increasing:
        return "IMPROVING" if higher_is_better else "WORSENING"

    if decreasing:
        return "WORSENING" if higher_is_better else "IMPROVING"

    return "STABLE"


def count_consecutive_increases(
    values: list[Decimal],
) -> int:

    if len(values) < 2:
        return 0

    count = 0

    for i in range(
        len(values) - 1,
        0,
        -1,
    ):
        if values[i] > values[i - 1]:
            count += 1
        else:
            break

    return count
