import pytest

from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.moment.player.action.shot import Shot, ShotResult
from hiddenfb.mappings.domain.moment.player.action import (
    GOAL_TAG,
    MISSED_SHOT_TAGS,
    SHOT_EVENT_ID,
    PlayerActionMapper,
)
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__player_action_mapper__creates_goal_from_wyscout_event():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=SHOT_EVENT_ID, tags=[WyscoutEventTag(tag_id=GOAL_TAG)]
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.GOAL


@pytest.mark.parametrize("tag_id", (MISSED_SHOT_TAGS))
def test__player_action_mapper__creates_missed_shot_from_wyscout_event(tag_id: int):
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=SHOT_EVENT_ID, tags=[WyscoutEventTag(tag_id=tag_id)]
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.MISS


def test__player_action_mapper__creates_saved_shot_from_wyscout_event():
    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        event_id=SHOT_EVENT_ID,
    )

    player_action_mapper = PlayerActionMapper()
    result: PlayerAction = player_action_mapper.from_wyscout_event(event)

    assert isinstance(result, Shot) and result.result is ShotResult.SAVE
