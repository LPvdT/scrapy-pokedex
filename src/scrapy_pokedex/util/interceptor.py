import itertools
import logging
from types import FrameType
from typing import cast

from loguru import logger

__all__ = ["_setup_loguru_logging_intercept", "InterceptHandler"]


class InterceptHandler(logging.Handler):
    """Logs to loguru from Python logging module"""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1
        logger_with_opts = logger.opt(depth=depth, exception=record.exc_info)

        try:
            logger_with_opts.log(level, "{}", record.getMessage())
        except Exception as e:
            safe_msg = getattr(record, "msg", None) or str(record)
            logger_with_opts.warning(
                "Exception logging the following native logger message: {}, {!r}",
                safe_msg,
                e,
            )


def _setup_loguru_logging_intercept(level=logging.DEBUG, modules=()) -> None:
    logging.basicConfig(handlers=[InterceptHandler()], level=level)

    for logger_name in itertools.chain(("",), modules):
        mod_logger = logging.getLogger(logger_name)
        mod_logger.handlers = [InterceptHandler(level=level)]
        mod_logger.propagate = False
