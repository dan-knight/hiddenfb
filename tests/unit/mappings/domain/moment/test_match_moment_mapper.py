from unittest.mock import MagicMock

from hiddenfb.domain.match import Match
from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.mappings.domain.moment.match import MatchMomentMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.test.domain.match import MatchTestUtility
from hiddenfb.test.domain.moment.match import MatchMomentTestUtility
from hiddenfb.test.schemas.data.metrica.event import MetricaEventTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__match_moment_mapper__creates_from_wyscout_event():
    match_utility = MatchTestUtility()
    match_: Match = match_utility.create_match(match_id=123)

    match_moment_utility = MatchMomentTestUtility(match_utility=match_utility)
    match_moment: MatchMoment = match_moment_utility.create_match_moment(match=match_)

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        match_id=match_.match_id, event_time=match_moment.frame
    )

    mock_match_mapper = MagicMock()
    mock_match_mapper.from_wyscout_event.return_value = match_moment.match

    match_moment_mapper = MatchMomentMapper(match_mapper=mock_match_mapper)

    result: MatchMoment = match_moment_mapper.from_wyscout_event(event)
    match_moment_utility.assert_equal(result, match_moment)

def test__match_moment_mapper__creates_from_metrica_event():
    match_utility = MatchTestUtility()
    match_: Match = match_utility.create_match(match_id=123)

    frame: int = 104
    match_moment_utility = MatchMomentTestUtility(match_utility=match_utility)
    match_moment: MatchMoment = match_moment_utility.create_match_moment(match=match_, frame=frame)

    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        start_frame=frame
    )

    mock_match_mapper = MagicMock()
    mock_match_mapper.from_metrica_event.return_value = match_moment.match

    match_moment_mapper = MatchMomentMapper(match_mapper=mock_match_mapper)

    result: MatchMoment = match_moment_mapper.from_metrica_event(event, match_id=match_.match_id)
    match_moment_utility.assert_equal(result, match_moment)

