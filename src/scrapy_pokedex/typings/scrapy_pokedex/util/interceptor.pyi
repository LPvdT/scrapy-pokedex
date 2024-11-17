import logging

__all__ = ["_setup_loguru_logging_intercept", "InterceptHandler"]

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None: ...

def _setup_loguru_logging_intercept(level=..., modules=()) -> None: ...
