from hiddenfb.domain.match import Match
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class MatchMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> Match:
        return Match(match_id=event.match_id)

    def from_metrica_event(self, event: MetricaEvent, match_id: int) -> Match:
        return Match(match_id=match_id)
