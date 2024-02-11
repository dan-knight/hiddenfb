from typing import Any, Dict
from marshmallow import ValidationError

import pytest
from hiddenfb.schemas.data.wyscout.event.schema import WyscoutEventPositionSchema
from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__wyscout_event_position_schema__x_is_required():
    event_utility = WyscoutEventTestUtility()
    position: WyscoutEventPosition = event_utility.create_event_position()

    json_position: Dict[str, Any] = event_utility.position_to_json(position)
    x_key: str = "x"
    json_position[x_key] = None

    schema = WyscoutEventPositionSchema()

    with pytest.raises(ValidationError, match=x_key):
        schema.load(json_position)
    
def test__wyscout_event_position_schema__y_is_required():
    event_utility = WyscoutEventTestUtility()
    position: WyscoutEventPosition = event_utility.create_event_position()

    json_position: Dict[str, Any] = event_utility.position_to_json(position)
    y_key: str = "y"
    json_position[y_key] = None

    schema = WyscoutEventPositionSchema()

    with pytest.raises(ValidationError, match=y_key):
        schema.load(json_position)
