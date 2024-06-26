from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.mappings.domain.match import MatchMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class MatchMomentMapper:
    def __init__(self, match_mapper: MatchMapper):
        self._match_mapper: MatchMapper = match_mapper

    def from_wyscout_event(self, event: WyscoutEvent) -> MatchMoment:
        return MatchMoment(
            match=self._match_mapper.from_wyscout_event(event), frame=event.event_time
        )

    def from_metrica_event(self, event: MetricaEvent, match_id: int) -> MatchMoment:
        return MatchMoment(
            match=self._match_mapper.from_metrica_event(event, match_id=match_id),
            frame=event.start_frame,
        )
