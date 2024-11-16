import shlex
import subprocess
from pathlib import Path

from loguru import logger

DATA_ROOT_DIR = Path(__file__).parent.joinpath("data")
logger.debug(DATA_ROOT_DIR)

DATA_OUTPUT_DIR = DATA_ROOT_DIR.joinpath("output")
logger.debug(DATA_OUTPUT_DIR)

LOG_DIR = DATA_ROOT_DIR.joinpath("logs")
logger.debug(LOG_DIR)


for dir in [DATA_OUTPUT_DIR, LOG_DIR]:
    dir.mkdir(exist_ok=True, parents=True)


def run() -> None:
    cmd = shlex.split(
        f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath('pep').with_suffix('.json')} --logfile {LOG_DIR.joinpath('log.log')}"
    )
    print(cmd)
    subprocess.run(cmd)
