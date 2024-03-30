from hiddenfb.domain.match import Match
from hiddenfb.mappings.domain.match import MatchMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.test.domain.match import MatchTestUtility
from hiddenfb.test.schemas.data.metrica.event import MetricaEventTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__match_mapper__creates_from_wyscout_event():
    match_utility = MatchTestUtility()
    match_: Match = match_utility.create_match()

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(match_id=match_.match_id)

    mapper = MatchMapper()
    result: Match = mapper.from_wyscout_event(event)

    match_utility.assert_equal(result, match_)


def test__match_mapper__creates_from_metrica_event():
    match_utility = MatchTestUtility()
    match_: Match = match_utility.create_match(match_id=3)

    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event()

    mapper = MatchMapper()
    result: Match = mapper.from_metrica_event(event, match_id=match_.match_id)

    match_utility.assert_equal(result, match_)
