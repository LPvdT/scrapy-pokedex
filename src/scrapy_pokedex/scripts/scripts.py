import logging
import shlex
import subprocess
from pathlib import Path

from loguru import logger

from scrapy_pokedex.scripts.constants import DATA_DIR, DATA_OUTPUT_DIR, LOG_DIR

from ..util.interceptor import InterceptHandler


def _setup_filesystem() -> None:
    logger.add(
        LOG_DIR.joinpath("system_log").with_suffix(".log"),
        level="DEBUG",
        rotation="1 week",
    )

    # FIX: Not working; fix
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    logger.info("Setting up filesystem...")
    logger.debug(f"DATA_DIR: {DATA_DIR}")
    logger.debug(f"DATA_OUTPUT_DIR: {DATA_OUTPUT_DIR}")
    logger.debug(f"LOG_DIR: {LOG_DIR}")

    for dir in [DATA_OUTPUT_DIR, LOG_DIR]:
        dir.mkdir(exist_ok=True, parents=True)


def run() -> None:
    _setup_filesystem()

    SPIDER = "pokedex_list"

    cmd = shlex.split(
        f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath('pep').with_suffix('.json')} --logfile {LOG_DIR.joinpath('scrapy_log').with_suffix('.log')} {SPIDER}"
    )
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd, cwd=Path(__file__).parents[1])


def types() -> None:
    _setup_filesystem()

    # TODO: Destructure package name and stub path
    logger.info("Deleting existing stubs...")
    subprocess.check_output(shlex.split("rm -rf src/scrapy_pokedex/typings"))

    cmd = shlex.split("stubgen -p scrapy_pokedex -o src/scrapy_pokedex/typings")
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)
