from typing import (
    TYPE_CHECKING,
    Any,
    Generic,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    TypeVar,
    cast,
    overload,
)

from marshmallow import Schema, types

T = TypeVar("T")


class GenericSchema(Schema, Generic[T]):
    if TYPE_CHECKING:

        @overload
        def load(
            self,
            data: Iterable[Mapping[str, Any]],
            *,
            many: Literal[True],
            partial: types.StrSequenceOrSet | bool | None = None,
            unknown: Optional[str] = None,
        ) -> List[T]: ...

        @overload
        def load(
            self,
            data: Iterable[Mapping[str, Any]],
            *,
            many: None = None,
            partial: types.StrSequenceOrSet | bool | None = None,
            unknown: Optional[str] = None,
        ) -> List[T]: ...

        @overload
        def load(
            self,
            data: Mapping[str, Any],
            *,
            many: Literal[False],
            partial: types.StrSequenceOrSet | bool | None = None,
            unknown: Optional[str] = None,
        ) -> T: ...

        @overload
        def load(
            self,
            data: Mapping[str, Any],
            *,
            many: None = None,
            partial: types.StrSequenceOrSet | bool | None = None,
            unknown: Optional[str] = None,
        ) -> T: ...

    def load(
        self,
        data: Mapping[str, Any] | Iterable[Mapping[str, Any]],
        *,
        many: bool | None = None,
        partial: types.StrSequenceOrSet | bool | None = None,
        unknown: Optional[str] = None,
    ):
        if many is None:
            many = not isinstance(data, dict)

        result = super().load(  # pyright: ignore[reportGeneralTypeIssues, reportUnknownVariableType]
            data, many=many, partial=partial, unknown=unknown
        )

        return cast(T if many is True else List[T], result)
