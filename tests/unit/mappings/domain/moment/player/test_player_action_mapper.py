import pytest

from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.moment.player.action.shot import Shot, ShotResult
from hiddenfb.mappings.domain.moment.player.action import PlayerActionMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.metrica.event.metadata import (
    MISSED_SHOT_SUBTYPES,
    MetricaEventType,
    MetricaShotEventSubtype,
)
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.metadata import (
    OFF_TARGET_SHOT_TAGS,
    ON_TARGET_SHOT_TAGS,
    POST_SHOT_TAGS,
    WyscoutEventID,
    WyscoutShotEventTag,
)
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag
from hiddenfb.test.schemas.data.metrica.event import MetricaEventTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__player_action_mapper__creates_goal_from_wyscout_event():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=WyscoutEventID.SHOT,
        tags=[WyscoutEventTag(tag_id=WyscoutShotEventTag.GOAL)],
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.GOAL


@pytest.mark.parametrize("tag_id", ([*OFF_TARGET_SHOT_TAGS, *POST_SHOT_TAGS]))
def test__player_action_mapper__creates_missed_shot_from_wyscout_event(tag_id: int):
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=WyscoutEventID.SHOT, tags=[WyscoutEventTag(tag_id=tag_id)]
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.MISS


@pytest.mark.parametrize("tag_id", (ON_TARGET_SHOT_TAGS))
def test__player_action_mapper__creates_saved_shot_from_wyscout_event(tag_id: int):
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=WyscoutEventID.SHOT, tags=[WyscoutEventTag(tag_id=tag_id)]
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.SAVE


def test__player_action_mapper__creates_goal_from_metrica_event():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        event_type=MetricaEventType.SHOT, event_subtype=MetricaShotEventSubtype.GOAL
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_metrica_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.GOAL


@pytest.mark.parametrize("event_subtype", (MISSED_SHOT_SUBTYPES))
def test__player_action_mapper__creates_missed_shot_from_metrica_event(
    event_subtype: MetricaShotEventSubtype,
):
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        event_type=MetricaEventType.SHOT, event_subtype=event_subtype
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_metrica_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.MISS


def test__player_action_mapper__creates_saved_shot_from_metrica_event():
    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        event_type=MetricaEventType.SHOT, event_subtype=MetricaShotEventSubtype.SAVE
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_metrica_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.SAVE


def test__player_action_mapper__errors_with_invalid_metrica_shot_subtype():
    invalid_event_subtype: str = "invalid"

    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        event_type=MetricaEventType.SHOT, event_subtype=invalid_event_subtype
    )

    player_action_mapper = PlayerActionMapper()
    with pytest.raises(ValueError, match=invalid_event_subtype):
        player_action_mapper.from_metrica_event(event)
