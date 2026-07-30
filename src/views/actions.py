"""
Application actions.
"""

from PySide6.QtGui import QAction, QKeySequence


class ApplicationActions:
    """Central repository for all application actions."""

    def __init__(self, parent) -> None:
        self.parent = parent

        self.open_file = QAction("&Open…", parent)
        self.open_file.setShortcut(QKeySequence.StandardKey.Open)
        self.open_file.setStatusTip("Open a localization file")

        self.save_file = QAction("&Save", parent)
        self.save_file.setShortcut(QKeySequence.StandardKey.Save)
        self.save_file.setStatusTip("Save the current file")

        self.exit = QAction("E&xit", parent)
        self.exit.setShortcut(QKeySequence.StandardKey.Quit)
        self.exit.setStatusTip("Exit Localization Studio")
        self.exit.triggered.connect(parent.close)

        self.about = QAction("&About", parent)
        self.about.setStatusTip("About Localization Studio")