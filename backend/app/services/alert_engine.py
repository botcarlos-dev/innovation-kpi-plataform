from app.models.alert import Alert


def create_trend_alert(
    project_id: int,
    kpi_id: int,
    current_value: float,
    previous_value: float,
    consecutive_increases: int,
):
    return Alert(
        project_id=project_id,
        kpi_id=kpi_id,
        severity="HIGH",
        alert_type="TREND",
        message=(
            f"KPI value increased for "
            f"{consecutive_increases} consecutive "
            f"measurement periods. "
            f"Current value: {current_value:.2f}. "
            f"Previous value: {previous_value:.2f}."
        ),
    )
