from typing import Any, Dict
from hiddenfb.domain.match import Match


class MatchTestUtility:
    def create_match(
        self,
        match_id: int = 45
    ) -> Match:
        return Match(
            match_id=match_id
        )
    
    def assert_equal(self, a: Match, b: Match) -> None:
        assert self.to_test_dict(a) == self.to_test_dict(b)
    
    def to_test_dict(self, match: Match) -> Dict[str, Any]:
        return match.__dict__
