"""
Application actions.
"""

from PySide6.QtGui import QAction, QKeySequence
from src.utils.icons import Icons

from PySide6.QtWidgets import QMessageBox

class ApplicationActions:
    """Central repository for all application actions."""

    def __init__(self, parent) -> None:
        self.parent = parent

        self.open_file = QAction("&Open…", parent)
        self.open_file.setShortcut(QKeySequence.StandardKey.Open)
        self.open_file.setStatusTip("Open a localization file")
        self.open_file.setIcon(Icons.open())

        self.save_file = QAction("&Save", parent)
        self.save_file.setShortcut(QKeySequence.StandardKey.Save)
        self.save_file.setStatusTip("Save the current file")
        self.save_file.setIcon(Icons.save())

        self.exit = QAction("E&xit", parent)
        self.exit.setShortcut(QKeySequence.StandardKey.Quit)
        self.exit.setStatusTip("Exit Localization Studio")
        self.exit.triggered.connect(parent.close)
        self.exit.setIcon(Icons.exit())

        self.about = QAction("&About", parent)
        self.about.setStatusTip("About Localization Studio")   
        self.about.setIcon(Icons.about())

        self.open_file.triggered.connect(
            lambda: QMessageBox.information(parent, "Test", "Ctrl+O détecté")
        )

        self.save_file.triggered.connect(
            lambda: QMessageBox.information(parent, "Test", "Ctrl+S détecté")
        )       