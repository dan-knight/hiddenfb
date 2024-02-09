
from typing import Any, Dict

from marshmallow import ValidationError
import pytest
from hiddenfb.schemas.data.metrica.tracking import MetricaTracking
from hiddenfb.schemas.data.metrica.tracking.schema import MetricaTrackingSchema
from hiddenfb.test.schemas.data.metrica.tracking import MetricaTrackingTestUtility


def test__metrica_tracking_schema__handles_all_valid_fields():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()
    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)

    schema = MetricaTrackingSchema()
    result: MetricaTracking = schema.load(json_tracking)

    assert result == tracking


def test__metrica_tracking_schema__id_is_required():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()

    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)
    id_key: str = "id"
    json_tracking[id_key] = None

    schema = MetricaTrackingSchema()

    with pytest.raises(ValidationError, match=id_key):
        schema.load(json_tracking)


def test__metrica_tracking_schema__id_does_not_allow_empty_string():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()

    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)
    id_key: str = "id"
    json_tracking[id_key] = ""

    schema = MetricaTrackingSchema()

    with pytest.raises(ValidationError, match=id_key):
        schema.load(json_tracking)


def test__metrica_tracking_schema__period_is_required():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()

    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)
    period_key: str = "period"
    json_tracking[period_key] = None

    schema = MetricaTrackingSchema()

    with pytest.raises(ValidationError, match=period_key):
        schema.load(json_tracking)


def test__metrica_tracking_schema__frame_is_required():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()

    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)
    frame_key: str = "frame"
    json_tracking[frame_key] = None

    schema = MetricaTrackingSchema()

    with pytest.raises(ValidationError, match=frame_key):
        schema.load(json_tracking)


def test__metrica_tracking_schema__time_is_required():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking()

    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)
    time_key: str = "time"
    json_tracking[time_key] = None

    schema = MetricaTrackingSchema()

    with pytest.raises(ValidationError, match=time_key):
        schema.load(json_tracking)


def test__metrica_tracking_schema__x_is_optional():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking(x=None)
    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)

    schema = MetricaTrackingSchema()
    result: MetricaTracking = schema.load(json_tracking)

    assert result.x is None


def test__metrica_tracking_schema__y_is_optional():
    tracking_utility = MetricaTrackingTestUtility()
    tracking: MetricaTracking = tracking_utility.create_tracking(y=None)
    json_tracking: Dict[str, Any] = tracking_utility.to_json(tracking)

    schema = MetricaTrackingSchema()
    result: MetricaTracking = schema.load(json_tracking)

    assert result.y is None
