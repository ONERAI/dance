import logging

from dance import config

logger = logging.getLogger("dance")

__version__ = "1.0.0-rc.1"
__all__ = [
    "config",
    "logger",
]
