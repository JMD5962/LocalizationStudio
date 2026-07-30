"""
Main application window.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
)

from src.version import (
    APP_NAME,
    APP_VERSION,
)


class MainWindow(QMainWindow):
    """
    Main window.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.resize(1200, 800)

        self._build_ui()

    def _build_ui(self) -> None:
        """
        Build the interface.
        """

        label = QLabel(APP_NAME)
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)
        