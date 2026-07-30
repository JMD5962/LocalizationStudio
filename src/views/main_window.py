"""
Main application window.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
)

from src.utils.settings import SettingsManager
from src.version import APP_NAME, APP_VERSION
from PySide6.QtGui import QAction

from src.views.actions import ApplicationActions

class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.settings = SettingsManager()

        self.actions = ApplicationActions(self)

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.resize(1200, 800)

        self._create_actions()
        self._create_menus()
        self._create_central_widget()
        self._create_statusbar()

        self._load_settings()

    def _create_central_widget(self) -> None:
        label = QLabel(APP_NAME)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

    def _create_statusbar(self) -> None:
        status = QStatusBar(self)
        status.showMessage("Ready")
        self.setStatusBar(status)

    def _load_settings(self) -> None:
        geometry = self.settings.value("mainwindow/geometry")

        if geometry is not None:
            self.restoreGeometry(geometry)

    def closeEvent(self, event) -> None:
        self.settings.set_value(
            "mainwindow/geometry",
            self.saveGeometry(),
        )

        super().closeEvent(event)

    def _create_actions(self) -> None:
        """Reserved for future action initialization."""
        # Les QAction sont déjà créées par ApplicationActions.
        pass


    def _create_menus(self) -> None:
        """Create the main menu bar."""

        menu_file = self.menuBar().addMenu("&File")
        menu_file.addAction(self.actions.open_file)
        menu_file.addAction(self.actions.save_file)
        menu_file.addSeparator()
        menu_file.addAction(self.actions.exit)

        menu_edit = self.menuBar().addMenu("&Edit")

        menu_tools = self.menuBar().addMenu("&Tools")

        menu_help = self.menuBar().addMenu("&Help")
        menu_help.addAction(self.actions.about)