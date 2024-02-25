from hiddenfb.domain.match import Match
from hiddenfb.mappings.domain.match import MatchMapper
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.test.domain.match import MatchTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__match_mapper__creates_from_wyscout_event():
    match_utility = MatchTestUtility()
    match: Match = match_utility.create_match()

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(match_id=match.match_id)

    mapper = MatchMapper()
    result: Match = mapper.from_wyscout_event(event)

    match_utility.assert_equal(result, match)
