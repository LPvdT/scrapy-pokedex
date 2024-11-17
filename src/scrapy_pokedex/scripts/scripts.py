import shlex
import subprocess
from typing import Callable

from loguru import logger

from ..util.constants import COMMANDS


@logger.catch
def command_factory(command_name: str, *args: str) -> Callable[[], None]:
    cmd = COMMANDS[command_name]

    @logger.catch
    def execute_command() -> None:
        try:
            if isinstance(cmd, str):
                cmd_to_run = shlex.split(cmd)
                logger.info(f"Running: {cmd_to_run}")
                subprocess.run(cmd_to_run, cwd="src" if "cwd" in args else None)
            elif isinstance(cmd, list):
                for command in cmd:
                    cmd_to_run = shlex.split(command)
                    logger.info(f"Running: {cmd_to_run}")
                    subprocess.run(cmd_to_run, cwd="src" if "cwd" in args else None)
        except KeyError:
            raise ValueError(f"Unknown command: {command_name}")

    return execute_command


scrape = command_factory("scrape", "cwd")
types = command_factory("gen_types")
setup_precommit = command_factory("setup_precommit")
precommit = command_factory("precommit")
