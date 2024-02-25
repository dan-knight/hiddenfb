from hiddenfb.domain.player import Player
from hiddenfb.mappings.domain.player import PlayerMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.test.domain.player import PlayerTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__player_mapper__creates_from_wyscout_event():
    player_utility = PlayerTestUtility()
    player = player_utility.create_player()

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(player_id=player.player_id)

    mapper = PlayerMapper()
    result: Player = mapper.from_wyscout_event(event)

    player_utility.assert_equal(result, player)
