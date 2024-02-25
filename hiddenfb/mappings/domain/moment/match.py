from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.mappings.domain.match import MatchMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class MatchMomentMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> MatchMoment:
        match_mapper = MatchMapper()
        return MatchMoment(
            match=match_mapper.from_wyscout_event(event),
            frame=event.event_time
        )
