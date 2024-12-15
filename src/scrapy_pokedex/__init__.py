import logging

from .settings import ENABLE_DEBUG
from .util.fs import _setup_filesystem
from .util.interceptor import _setup_loguru_logging_intercept

_setup_loguru_logging_intercept(
    level=logging.INFO if not ENABLE_DEBUG else logging.DEBUG,
    modules=("scrapy_pokedex",),
)
_setup_filesystem(ENABLE_DEBUG)
