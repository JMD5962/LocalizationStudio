"""
Application paths.
"""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]

LOGS_DIR = ROOT_DIR / "logs"
RESOURCES_DIR = ROOT_DIR / "resources"

LOGS_DIR.mkdir(exist_ok=True)
RESOURCES_DIR.mkdir(exist_ok=True)