from .util.fs import _setup_filesystem
from .util.interceptor import _setup_loguru_logging_intercept

_setup_loguru_logging_intercept(modules=("scrapy_pokedex",))
_setup_filesystem()


def main() -> None:
    print("Hello from scrapy-pokedex!")
