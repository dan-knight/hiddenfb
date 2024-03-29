from unittest.mock import MagicMock

from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.mappings.domain.moment.player import PlayerMomentMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.test.domain.moment.player import PlayerMomentTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__player_moment_mapper__creates_from_wyscout_event():
    player_moment_utility = PlayerMomentTestUtility()
    player_moment: PlayerMoment[PlayerAction] = (
        player_moment_utility.create_player_moment(
            player=MagicMock(),
            match_moment=MagicMock(),
            player_action=MagicMock(),
            coordinates=MagicMock(),
        )
    )

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event()

    mock_player_mapper = MagicMock()
    mock_player_mapper.from_wyscout_event.return_value = player_moment.player

    mock_match_moment_mapper = MagicMock()
    mock_match_moment_mapper.from_wyscout_event.return_value = (
        player_moment.match_moment
    )

    mock_player_action_mapper = MagicMock()
    mock_player_action_mapper.from_wyscout_event.return_value = player_moment.action

    mock_coordinate_mapper = MagicMock()
    mock_coordinate_mapper.from_wyscout_event.return_value = player_moment.coordinates

    player_moment_mapper = PlayerMomentMapper(
        player_mapper=mock_player_mapper,
        match_moment_mapper=mock_match_moment_mapper,
        player_action_mapper=mock_player_action_mapper,
        coordinate_mapper=mock_coordinate_mapper,
    )
    result: PlayerMoment[PlayerAction] = player_moment_mapper.from_wyscout_event(event)

    player_moment_utility.assert_equal(result, player_moment)
