from typing import Any, Mapping

from marshmallow.fields import Field, Float, Integer, String

NA_VALUE: str = "NaN"


class NAField(Field):
    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ):
        na_value = str(
            self.metadata.get(  # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
                "na_value", NA_VALUE
            )
        )

        if value == na_value:
            return None

        return super()._deserialize(  # pyright: ignore[reportUnknownMemberType]
            value, attr, data, **kwargs
        )


class NAString(NAField, String):
    ...


class NAInteger(NAField, Integer):
    ...


class NAFloat(NAField, Float):
    ...


class EmptyField(Field):
    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ):
        if value == "":
            return None
        
        return super()._deserialize(  # pyright: ignore[reportUnknownMemberType]
            value, attr, data, **kwargs
        )


class EmptyString(EmptyField, String):
    ...


class NonEmptyField(Field):
    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ):
        if value == "":
            value = None
        
        return super()._deserialize(  # pyright: ignore[reportUnknownMemberType]
            value, attr, data, **kwargs
        )

class NonEmptyString(NonEmptyField, String):
    ...
