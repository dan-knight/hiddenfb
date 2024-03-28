from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.mappings.domain.moment.match import MatchMomentMapper
from hiddenfb.mappings.domain.player import PlayerMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class PlayerMomentMapper:
    def __init__(
        self, player_mapper: PlayerMapper, match_moment_mapper: MatchMomentMapper
    ):
        self._player_mapper: PlayerMapper = player_mapper
        self._match_moment_mapper: MatchMomentMapper = match_moment_mapper

    def from_wyscout_event(self, event: WyscoutEvent):
        return PlayerMoment(
            player=self._player_mapper.from_wyscout_event(event),
            match_moment=self._match_moment_mapper.from_wyscout_event(event),
            action=None,
        )
