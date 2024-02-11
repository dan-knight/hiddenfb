from typing import Any, Dict

import pytest
from marshmallow import ValidationError

from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.schema import WyscoutEventSchema
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__wyscout_event_schema__handles_all_valid_fields():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()
    json_event: Dict[str, Any] = event_utility.to_json(event)

    schema = WyscoutEventSchema()
    result = schema.load(json_event)

    assert result == event


def test__wyscout_event_schema__event_id_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_id_key: str = "id"
    json_event[event_id_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=event_id_key):
        schema.load(json_event)


def test__wyscout_event_schema__match_id_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    match_id_key: str = "matchId"
    json_event[match_id_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=match_id_key):
        schema.load(json_event)


def test__wyscout_event_schema__player_id_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    player_id_key: str = "playerId"
    json_event[player_id_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=player_id_key):
        schema.load(json_event)


def test__wyscout_event_schema__team_id_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    team_id_key: str = "teamId"
    json_event[team_id_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=team_id_key):
        schema.load(json_event)


def test__wyscout_event_schema__period_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    period_key: str = "matchPeriod"
    json_event[period_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=period_key):
        schema.load(json_event)


def test__wyscout_event_schema__period_does_not_allow_empty_string():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    period_key: str = "matchPeriod"
    json_event[period_key] = ""

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=period_key):
        schema.load(json_event)


def test__wyscout_event_schema__event_time_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_time_key: str = "eventTime"
    json_event[event_time_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=event_time_key):
        schema.load(json_event)


def test__wyscout_event_schema__event_type_id_is_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_type_id_key: str = "eventId"
    json_event[event_type_id_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=event_type_id_key):
        schema.load(json_event)


def test__wyscout_event_schema__event_name_does_not_allow_empty_string():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    event_name_key: str = "eventName"
    json_event[event_name_key] = ""

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=event_name_key):
        schema.load(json_event)


def test__wyscout_event_schema__sub_event_id_allows_empty_string():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    json_event["subEventId"] = ""

    schema = WyscoutEventSchema()
    result = schema.load(json_event)

    assert result.sub_event_id == None


def test__wyscout_event_schema__sub_event_name_allows_empty_string():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    json_event["subEventName"] = ""

    schema = WyscoutEventSchema()
    result = schema.load(json_event)

    assert result.sub_event_name == None


def test__wyscout_event_schema__tags_are_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    tags_key: str = "tags"
    json_event[tags_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=tags_key):
        schema.load(json_event)


def test__wyscout_event_schema__positions_are_required():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    json_event: Dict[str, Any] = event_utility.to_json(event)
    positions_key: str = "positions"
    json_event[positions_key] = None

    schema = WyscoutEventSchema()

    with pytest.raises(ValidationError, match=positions_key):
        schema.load(json_event)
