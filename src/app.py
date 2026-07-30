"""
Application bootstrap.
"""

from PySide6.QtWidgets import QApplication

from src.version import (
    APP_DOMAIN,
    APP_NAME,
    APP_ORGANIZATION,
)


def create_application() -> QApplication:
    """
    Create and configure the Qt application.
    """
    app = QApplication([])

    app.setApplicationName(APP_NAME)
    app.setOrganizationName(APP_ORGANIZATION)
    app.setOrganizationDomain(APP_DOMAIN)

    return app
