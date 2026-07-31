"""
Application logging configuration.
"""

import sys

from loguru import logger

from src.core.constants import LOG_FILENAME
from src.core.paths import LOGS_DIR


def configure_logging() -> None:
    """Configure Loguru."""

    logger.remove()

    logger.add(
        sys.stderr,
        level="INFO",
        colorize=True,
    )

    logger.add(
        LOGS_DIR / LOG_FILENAME,
        rotation="10 MB",
        retention=10,
        encoding="utf-8",
        level="DEBUG",
    )

    logger.info("Localization Studio started.")