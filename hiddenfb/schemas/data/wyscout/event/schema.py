from typing import Any, Mapping

from marshmallow import fields, post_load

import hiddenfb.utility.schema.fields as custom_fields
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag
from hiddenfb.utility.schema import GenericSchema


class WyscoutEventTagSchema(GenericSchema[WyscoutEventTag]):
    tag_id = fields.Integer(required=True, data_key="id")

    @post_load
    def _deserialize_tag(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> WyscoutEventTag:
        return WyscoutEventTag(**data)


class WyscoutEventPositionSchema(GenericSchema[WyscoutEventPosition]):
    x = fields.Integer(required=True)
    y = fields.Integer(required=True)

    @post_load
    def _deserialize_position(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> WyscoutEventPosition:
        return WyscoutEventPosition(**data)


class WyscoutEventSchema(GenericSchema[WyscoutEvent]):
    event_id = fields.Integer(required=True, data_key="id")
    player_id = fields.Integer(required=True, data_key="playerId")
    team_id = fields.Integer(required=True, data_key="teamId")
    match_id = fields.Integer(required=True, data_key="matchId")
    period = custom_fields.NonEmptyString(required=True, data_key="matchPeriod")
    event_time = fields.Float(required=True, data_key="eventSec")
    event_type_id = fields.Integer(required=True, data_key="eventId")
    event_type_name = custom_fields.NonEmptyString(required=True, data_key="eventName")
    sub_event_id = custom_fields.NAInteger(
        metadata={"na_value": ""}, required=True, data_key="subEventId"
    )
    sub_event_name = custom_fields.EmptyString(required=True, data_key="subEventName")
    tags = fields.Nested(
        WyscoutEventTagSchema(many=True), required=True, data_key="tags"
    )
    positions = fields.Nested(WyscoutEventPositionSchema(many=True))

    @post_load
    def _deserialize_event(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> WyscoutEvent:
        return WyscoutEvent(**data)
