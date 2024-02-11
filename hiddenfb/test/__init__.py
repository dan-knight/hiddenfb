from typing import Any, TypeVar

OptionalString = TypeVar("OptionalString", bound=str | None)


class TestUtility:
    def _to_string(
        self, x: Any, default: OptionalString = None
    ) -> str | OptionalString:
        return str(x) if x is not None else default
