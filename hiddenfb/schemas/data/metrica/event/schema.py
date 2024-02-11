from typing import Any, Mapping

from marshmallow import fields, post_load

import hiddenfb.utility.schema.fields as custom_fields
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.utility.schema import GenericSchema


class MetricaEventSchema(GenericSchema[MetricaEvent]):
    team = custom_fields.NonEmptyString(required=True, data_key="Team")
    event_type = custom_fields.NonEmptyString(required=True, data_key="Type")
    event_subtype = custom_fields.EmptyString(required=True, data_key="Subtype")
    period = fields.Integer(required=True, data_key="Period")
    start_frame = fields.Integer(required=True, data_key="Start Frame")
    end_frame = fields.Integer(required=True, data_key="End Frame")
    start_time = fields.Float(required=True, data_key="Start Time [s]")
    end_time = fields.Float(required=True, data_key="End Time [s]")
    player_from = custom_fields.NonEmptyString(required=True, data_key="From")
    player_to = custom_fields.EmptyString(required=True, data_key="To")
    start_x = custom_fields.NAFloat(required=True, data_key="Start X")
    start_y = custom_fields.NAFloat(required=True, data_key="Start Y")
    end_x = custom_fields.NAFloat(required=True, data_key="End X")
    end_y = custom_fields.NAFloat(required=True, data_key="End Y")

    @post_load
    def _deserialize_event(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> MetricaEvent:
        return MetricaEvent(**data)
