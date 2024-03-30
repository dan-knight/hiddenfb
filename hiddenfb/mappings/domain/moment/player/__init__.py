from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.mappings.domain.coordinates import CoordinatesMapper
from hiddenfb.mappings.domain.moment.match import MatchMomentMapper
from hiddenfb.mappings.domain.moment.player.action import PlayerActionMapper
from hiddenfb.mappings.domain.player import PlayerMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class PlayerMomentMapper:
    def __init__(
        self,
        player_mapper: PlayerMapper,
        match_moment_mapper: MatchMomentMapper,
        player_action_mapper: PlayerActionMapper,
        coordinate_mapper: CoordinatesMapper,
    ):
        self._player_mapper: PlayerMapper = player_mapper
        self._match_moment_mapper: MatchMomentMapper = match_moment_mapper
        self._player_action_mapper: PlayerActionMapper = player_action_mapper
        self._coordinate_mapper: CoordinatesMapper = coordinate_mapper

    def from_wyscout_event(self, event: WyscoutEvent):
        return PlayerMoment[PlayerAction](
            player=self._player_mapper.from_wyscout_event(event),
            match_moment=self._match_moment_mapper.from_wyscout_event(event),
            action=self._player_action_mapper.from_wyscout_event(event),
            coordinates=self._coordinate_mapper.from_wyscout_event(event),
        )

    def from_metrica_event(self, event: MetricaEvent, match_id: int):
        return PlayerMoment[PlayerAction](
            player=self._player_mapper.from_metrica_event(event),
            match_moment=self._match_moment_mapper.from_metrica_event(
                event, match_id=match_id
            ),
            action=self._player_action_mapper.from_metrica_event(event),
            coordinates=self._coordinate_mapper.from_metrica_event(event),
        )
