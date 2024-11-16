import logging
import shlex
import subprocess
from pathlib import Path

from loguru import logger

from util.interceptor import InterceptHandler

DATA_DIR = Path(__file__).parents[1] / "data"
DATA_OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = DATA_DIR / "logs"


logger.add(
    LOG_DIR.joinpath("system_log").with_suffix(".log"),
    level="DEBUG",
    rotation="1 week",
)

# FIX: Not working; fix
logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)


def _setup_filesystem() -> None:
    """
    Sets up the file system layout for the data collection pipeline.

    Creates the output and log directories if they do not already exist.
    """

    logger.info("Setting up filesystem...")
    logger.debug(f"DATA_DIR: {DATA_DIR}")
    logger.debug(f"DATA_OUTPUT_DIR: {DATA_OUTPUT_DIR}")
    logger.debug(f"LOG_DIR: {LOG_DIR}")

    for dir in [DATA_OUTPUT_DIR, LOG_DIR]:
        dir.mkdir(exist_ok=True, parents=True)


def run() -> None:
    """
    Executes a Scrapy crawl command to collect data and save it as a JSON file.

    The function constructs a command using the `shlex.split` method to run
    a Scrapy spider, which outputs the data to a JSON file located in the
    `DATA_OUTPUT_DIR` and logs the process in the `LOG_DIR`. The command
    is then executed using `subprocess.run`.

    Returns:
        None
    """

    _setup_filesystem()

    SPIDER = "pokedex_list"

    cmd = shlex.split(
        f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath('pep').with_suffix('.json')} --logfile {LOG_DIR.joinpath('scrapy_log').with_suffix('.log')} {SPIDER}"
    )
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)
