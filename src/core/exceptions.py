"""
Application custom exceptions.
"""


class LocalizationStudioError(Exception):
    """Base application exception."""


class JsonFileError(LocalizationStudioError):
    """Raised when a JSON file cannot be loaded."""


class InvalidJsonError(JsonFileError):
    """Raised when JSON is invalid."""