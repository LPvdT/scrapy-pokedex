import shlex
import subprocess
from typing import Callable

from loguru import logger

from .constants import COMMANDS


@logger.catch
def command_factory(command_name: str, *args: str) -> Callable[[], None]:
    cmd = COMMANDS.get(command_name)
    if cmd is None:
        raise ValueError(f"Unknown command: {command_name}")

    cwd = "src" if "cwd" in args else None

    @logger.catch
    def execute_command() -> None:
        try:
            cmds = cmd if isinstance(cmd, list) else [cmd]
            for command in cmds:
                cmd_to_run = shlex.split(command)
                logger.info(f"Running: {cmd_to_run}")
                subprocess.run(cmd_to_run, cwd=cwd)
        except KeyError:
            raise ValueError(f"Unknown command: {command_name}")

    return execute_command
