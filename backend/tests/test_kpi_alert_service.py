from unittest.mock import Mock

from app.services.kpi_alert_service import (
    create_alert_for_measurement,
)


def test_healthy_measurement_does_not_create_alert():
    measurement = Mock()
    measurement.status = "HEALTHY"

    kpi = Mock()

    result = create_alert_for_measurement(
        db=Mock(),
        measurement=measurement,
        kpi=kpi,
    )

    assert result is None


def test_warning_measurement_creates_alert():
    db = Mock()

    measurement = Mock()
    measurement.id = 1
    measurement.project_id = 10
    measurement.kpi_id = 5
    measurement.status = "WARNING"
    measurement.value = 12.00

    kpi = Mock()
    kpi.id = 5
    kpi.name = "Budget Variance"
    kpi.unit = "%"

    # No existing alert
    db.query.return_value.filter.return_value.first.return_value = None

    result = create_alert_for_measurement(
        db=db,
        measurement=measurement,
        kpi=kpi,
    )

    assert result is not None
    assert result.severity == "WARNING"
    assert result.title == "Budget Variance - WARNING"
    assert "Budget Variance" in result.message
    assert "WARNING" in result.message
    assert result.project_id == 10
    assert result.kpi_id == 5
    assert result.measurement_id == 1
    assert result.acknowledged is False

    db.add.assert_called_once_with(result)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(result)


def test_critical_measurement_creates_alert():
    db = Mock()

    measurement = Mock()
    measurement.id = 2
    measurement.project_id = 20
    measurement.kpi_id = 8
    measurement.status = "CRITICAL"
    measurement.value = 18.50

    kpi = Mock()
    kpi.id = 8
    kpi.name = "Innovation ROI"
    kpi.unit = "%"

    # No existing alert
    db.query.return_value.filter.return_value.first.return_value = None

    result = create_alert_for_measurement(
        db=db,
        measurement=measurement,
        kpi=kpi,
    )

    assert result is not None
    assert result.severity == "CRITICAL"
    assert result.title == "Innovation ROI - CRITICAL"
    assert "Innovation ROI" in result.message
    assert "CRITICAL" in result.message
    assert result.project_id == 20
    assert result.kpi_id == 8
    assert result.measurement_id == 2
    assert result.acknowledged is False

    db.add.assert_called_once_with(result)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(result)


def test_existing_alert_is_not_duplicated():
    db = Mock()

    measurement = Mock()
    measurement.id = 3
    measurement.project_id = 30
    measurement.kpi_id = 3
    measurement.status = "CRITICAL"

    kpi = Mock()
    kpi.id = 3
    kpi.name = "Project Progress"
    kpi.unit = "%"

    existing_alert = Mock()
    existing_alert.id = 99
    existing_alert.severity = "CRITICAL"

    db.query.return_value.filter.return_value.first.return_value = existing_alert

    result = create_alert_for_measurement(
        db=db,
        measurement=measurement,
        kpi=kpi,
    )

    assert result is existing_alert

    db.add.assert_not_called()
    db.commit.assert_not_called()
    db.refresh.assert_not_called()
