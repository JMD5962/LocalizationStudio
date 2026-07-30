"""
Persistent application settings.
"""

from PySide6.QtCore import QSettings


class SettingsManager:
    """Wrapper around QSettings."""

    def __init__(self) -> None:
        self._settings = QSettings()

    def value(self, key: str, default=None):
        return self._settings.value(key, default)

    def set_value(self, key: str, value) -> None:
        self._settings.setValue(key, value)

    def contains(self, key: str) -> bool:
        return self._settings.contains(key)
    