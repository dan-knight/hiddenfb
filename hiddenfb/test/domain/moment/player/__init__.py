from typing import Any, Dict
from hiddenfb.domain.coordinate.pitch import PitchCoordinates
from hiddenfb.domain.moment.match import MatchMoment

from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.player import Player
from hiddenfb.test.domain.coordinates.pitch import PitchCoordinatesTestUtility
from hiddenfb.test.domain.match import MatchTestUtility
from hiddenfb.test.domain.moment.match import MatchMomentTestUtility
from hiddenfb.test.domain.moment.player.action import PlayerActionTestUtility
from hiddenfb.test.domain.player import PlayerTestUtility


class PlayerMomentTestUtility:
    def create_player_moment(
        self,
        player: Player | None = None,
        match_moment: MatchMoment | None = None,
        player_action: PlayerAction | None = None,
        coordinates: PitchCoordinates | None = None,
    ) -> PlayerMoment[PlayerAction]:
        player_utility = PlayerTestUtility()
        match_utility = MatchTestUtility()
        match_moment_utility = MatchMomentTestUtility(match_utility=match_utility)
        player_action_utility = PlayerActionTestUtility()
        coordinate_utility = PitchCoordinatesTestUtility()

        if player is None:
            player = player_utility.create_player()

        if match_moment is None:
            match_moment = match_moment_utility.create_match_moment()

        if player_action is None:
            player_action = player_action_utility.create_player_action()

        if coordinates is None:
            coordinates = coordinate_utility.create_coordinates()

        return PlayerMoment(
            player=player,
            match_moment=match_moment,
            action=player_action,
            coordinates=coordinates,
        )

    def assert_equal(
        self, a: PlayerMoment[PlayerAction], b: PlayerMoment[PlayerAction]
    ):
        assert self.to_test_dict(a) == self.to_test_dict(b)

    def to_test_dict(self, x: PlayerMoment[PlayerAction]) -> Dict[str, Any]:
        return {
            "player": x.player,
            "match_moment": x.match_moment,
            "action": x.action,
            "coordinates": x.coordinates
        }
