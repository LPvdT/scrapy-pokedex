import logging
import sys

from loguru import logger

from .constants import DATA_DIR, DATA_OUTPUT_DIR, LOG_DIR

__all__ = ["_setup_filesystem"]


def _setup_filesystem() -> None:
    logger.add(sys.stdout, level=logging.INFO)

    logger.add(
        LOG_DIR.joinpath("info_log").with_suffix(".log"),
        level=logging.INFO,
        rotation="1 week",
    )

    logger.add(
        LOG_DIR.joinpath("debug_log").with_suffix(".log"),
        level=logging.DEBUG,
        rotation="1 day",
    )

    logger.info("Setting up filesystem:")
    logger.debug(f"DATA_DIR: {DATA_DIR}")
    logger.debug(f"DATA_OUTPUT_DIR: {DATA_OUTPUT_DIR}")
    logger.debug(f"LOG_DIR: {LOG_DIR}")

    for dir in [DATA_OUTPUT_DIR, LOG_DIR]:
        dir.mkdir(exist_ok=True, parents=True)
