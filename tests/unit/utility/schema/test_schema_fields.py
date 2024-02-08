from typing import Any, Dict, Mapping

from marshmallow import ValidationError, post_load
import pytest

from hiddenfb.utility.schema import GenericSchema
from hiddenfb.utility.schema.fields import NAField, EmptyField, NA_VALUE as DEFAULT_NA_VALUE, NonEmptyString

CUSTOM_NA_VALUE: str = "NA"


class NASchema(GenericSchema[Dict[str, Any]]):
    na = NAField()
    custom_na = NAField(metadata={"na_value": CUSTOM_NA_VALUE})

    @post_load
    def _deserialize_event(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> Dict[str, Any]:
        return {**data}


class EmptySchema(GenericSchema[Dict[str, Any]]):
    empty = EmptyField()
    non_empty = NonEmptyString()

    @post_load
    def _deserialize_event(
        self, data: Mapping[str, Any], **kwargs: Mapping[str, Any]
    ) -> Dict[str, Any]:
        return {**data}


def test__na_field__uses_default_na_value():
    value = {"na": DEFAULT_NA_VALUE}

    schema = NASchema(many=True)
    result = schema.load(value)

    assert result["na"] is None


def test__na_field__uses_given_na_value():
    na_value: str = CUSTOM_NA_VALUE
    value = {"custom_na": na_value}

    schema = NASchema()
    result: Dict[str, Any] = schema.load(value)

    assert result["custom_na"] is None


def test__empty_field__handles_empty_string():
    value = {"empty": ""}

    schema = EmptySchema()
    result: Dict[str, Any] = schema.load(value)

    assert result["empty"] is None


def test__empty_field__allows_value():
    x: str = "test"
    value = {"empty": x}

    schema = EmptySchema()
    result: Dict[str, Any] = schema.load(value)

    assert result["empty"] == x


def test__non_empty_string_field__does_not_allow_empty_string():
    empty_key: str = "non_empty"
    value = {empty_key: ""}

    schema = EmptySchema()
    
    with pytest.raises(ValidationError, match=empty_key):
        schema.load(value)


def test__non_empty_string_field__allows_value():
    x: str = "test"
    value = {"non_empty": x}

    schema = EmptySchema()
    result: Dict[str, Any] = schema.load(value)

    assert result["non_empty"] == x
