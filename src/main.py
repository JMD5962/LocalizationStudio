"""
Localization Studio entry point.
"""

import sys

from src.app import create_application
from src.views.main_window import MainWindow
from src.services.logging_service import configure_logging

def main() -> int:
    configure_logging()
    app = create_application()

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
    