from .constants import COMMANDS as COMMANDS
from typing import Callable

def command_factory(command_name: str, *args: str) -> Callable[[], None]: ...
