class BaseNumberError(ValueError):
    def _format_message(self, message: str, value: float, attribute_name: str) -> str:
        result: str = message
        if attribute_name != "":
            result = f'"{attribute_name}" {result.lower()}'
        result += f"(received {value})."

        return result


class NegativeNumberError(BaseNumberError):
    def __init__(self, value: float, attribute_name: str = ""):
        message: str = self._format_message(
            message="Value cannot be negative",
            value=value,
            attribute_name=attribute_name,
        )

        super().__init__(message)


class ZeroNumberError(BaseNumberError):
    def __init__(self, value: float, attribute_name: str = ""):
        message: str = self._format_message(
            message="Value cannot be zero", value=value, attribute_name=attribute_name
        )

        super().__init__(message)


class PositiveNumberError(BaseNumberError):
    def __init__(self, value: float, attribute_name: str = ""):
        message: str = self._format_message(
            message="Value cannot be positive",
            value=value,
            attribute_name=attribute_name,
        )

        super().__init__(message)


class DecimalNumberError(BaseNumberError):
    def __init__(self, value: float, attribute_name: str = ""):
        message: str = self._format_message(
            message="Value must be an integer",
            value=value,
            attribute_name=attribute_name,
        )

        super().__init__(message)
