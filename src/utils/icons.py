"""
QtAwesome icon factory.
"""

import qtawesome as qta


class Icons:
    """Application icon factory."""

    @staticmethod
    def open():
        return qta.icon("fa6s.folder-open")

    @staticmethod
    def save():
        return qta.icon("fa6s.floppy-disk")

    @staticmethod
    def exit():
        return qta.icon("fa6s.right-from-bracket")

    @staticmethod
    def about():
        return qta.icon("fa6s.circle-info")
    