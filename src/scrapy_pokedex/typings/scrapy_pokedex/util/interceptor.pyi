import logging

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None: ...
