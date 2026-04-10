from typing import Any
import logging
import environ
from pathlib import Path

# Base directory = beamstack_be/ (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)


def get_env(variable: str) -> Any:
    env = environ.Env(
        DEBUG=(bool, False)
    )

    environ.Env.read_env(BASE_DIR / '.env')

    loaded_env = env(variable)

    if loaded_env is None:
        logger.warning("Warning: ${variable} is invalid or missing in env config")

    return loaded_env
