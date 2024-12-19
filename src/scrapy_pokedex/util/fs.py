import logging

from loguru import logger

from .constants import DATA_DIR, DATA_OUTPUT_DIR, LOG_DIR

__all__ = ["_setup_filesystem"]


def _setup_filesystem(enable_debug: bool = False) -> None:
    logger.add(
        LOG_DIR.joinpath("info_log").with_suffix(".log"),
        level=logging.INFO,
        backtrace=False,
        diagnose=True,  # DEBUG
        rotation="1 week",
    )

    if enable_debug:
        logger.add(
            LOG_DIR.joinpath("debug_log").with_suffix(".log"),
            level=logging.DEBUG,
            rotation="1 day",
        )

    for dir in [DATA_OUTPUT_DIR, LOG_DIR]:
        if not dir.exists():
            dir.mkdir(parents=True)

            logger.warning("Filesystem not set up. Setting up filesystem:")
            logger.info(f"DATA_DIR: {DATA_DIR}")
            logger.info(f"DATA_OUTPUT_DIR: {DATA_OUTPUT_DIR}")
            logger.info(f"LOG_DIR: {LOG_DIR}")
