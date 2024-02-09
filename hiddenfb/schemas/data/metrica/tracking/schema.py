from typing import Any, Mapping
from marshmallow import fields, post_load

import hiddenfb.utility.schema.fields as custom_fields
from hiddenfb.schemas.data.metrica.tracking import MetricaTracking
from hiddenfb.utility.schema import GenericSchema


class MetricaTrackingSchema(GenericSchema[MetricaTracking]):
    id = custom_fields.NonEmptyString(required=True)
    period = fields.Integer(required=True)
    frame = fields.Integer(required=True)
    time = fields.Float(required=True)
    x = custom_fields.NAFloat(required=True)
    y = custom_fields.NAFloat(required=True)

    @post_load
    def _deserialize_tracking(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> MetricaTracking:
        return MetricaTracking(**data)
