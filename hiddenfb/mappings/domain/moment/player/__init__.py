from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.mappings.domain.moment.match import MatchMomentMapper
from hiddenfb.mappings.domain.player import PlayerMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class PlayerMomentMapper:
    def from_wyscout_event(self, event: WyscoutEvent):
        player_mapper = PlayerMapper()
        match_moment_mapper = MatchMomentMapper()

        return PlayerMoment(
            player=player_mapper.from_wyscout_event(event),
            match_moment=match_moment_mapper.from_wyscout_event(event),
            action=None
        )