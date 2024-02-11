from typing import Any, Dict
from marshmallow import ValidationError

import pytest
from hiddenfb.schemas.data.wyscout.event.schema import WyscoutEventTagSchema
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__wyscout_event_tag_schema__tag_id_is_required():
    event_utility = WyscoutEventTestUtility()
    tag: WyscoutEventTag = event_utility.create_event_tag()

    json_tag: Dict[str, Any] = event_utility.tag_to_json(tag)
    tag_id_key: str = "id"
    json_tag[tag_id_key] = ""

    schema = WyscoutEventTagSchema()

    with pytest.raises(ValidationError, match=tag_id_key):
        schema.load(json_tag)
