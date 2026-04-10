import logging
from environ import Env
import environ
from pathlib import Path

# Base directory = beamstack_be/ (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)


def get_env(variable: str) -> Env:
    env = environ.Env(
        DEBUG=(bool, False)
    )

    environ.Env.read_env(BASE_DIR / '.env')

    if env(variable) is None:
        logger.warning("Warning: ${variable} is invalid or missing in env config")

    return env
