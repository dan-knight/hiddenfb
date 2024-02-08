import re
from typing import Any, Dict
from marshmallow import ValidationError

import pytest
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.metrica.event.schema import MetricaEventSchema
from hiddenfb.test.schemas.data.metrica.event import MetricaEventTestUtility


def test__metrica_event_schema__handles_all_valid_fields():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result == event


def test__metrica_event_schema__team_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    team_key: str = "Team"
    json_event[team_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=team_key):
        schema.load(json_event)


def test__metrica_event_schema__team_does_not_allow_empty_string():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    team_key: str = "Team"
    json_event[team_key] = ""

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=team_key):
        schema.load(json_event)


def test__metrica_event_schema__event_type_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_type_key: str = "Type"
    json_event[event_type_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=event_type_key):
        schema.load(json_event)


def test__metrica_event_schema__event_type_does_not_allow_empty_string():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_type_key: str = "Type"
    json_event[event_type_key] = ""

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=event_type_key):
        schema.load(json_event)


def test__metrica_event_schema__subtype_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(event_subtype=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.event_subtype is None


def test__metrica_event_schema__period_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    period_key: str = "Period"
    json_event[period_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=period_key):
        schema.load(json_event)


def test__metrica_event_schema__start_frame_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    start_frame_key: str = "Start Frame"
    json_event[start_frame_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=start_frame_key):
        schema.load(json_event)


def test__metrica_event_schema__end_frame_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    end_frame_key: str = "End Frame"
    json_event[end_frame_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=end_frame_key):
        schema.load(json_event)


def test__metrica_event_schema__start_time_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    start_time_key: str = "Start Time [s]"
    json_event[start_time_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=re.escape(start_time_key)):
        schema.load(json_event)


def test__metrica_event_schema__end_time_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    end_time_key: str = "End Time [s]"
    json_event[end_time_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=re.escape(end_time_key)):
        schema.load(json_event)


def test__metrica_event_schema__player_from_is_required():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    player_from_key: str = "From"
    json_event[player_from_key] = None

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=re.escape(player_from_key)):
        schema.load(json_event)


def test__metrica_event_schema__player_from_does_not_allow_empty_string():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    player_from_key: str = "From"
    json_event[player_from_key] = ""

    schema = MetricaEventSchema()

    with pytest.raises(ValidationError, match=player_from_key):
        schema.load(json_event)


def test__metrica_event_schema__player_to_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(player_to=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.player_to is None



def test__metrica_event_schema__start_x_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(start_x=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.start_x is None


def test__metrica_event_schema__start_y_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(start_y=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.start_y is None


def test__metrica_event_schema__end_x_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(end_x=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.end_x is None


def test__metrica_event_schema__end_y_is_optional():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(end_y=None)
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = MetricaEventSchema()
    result: MetricaEvent = schema.load(json_event)

    assert result.end_y is None
