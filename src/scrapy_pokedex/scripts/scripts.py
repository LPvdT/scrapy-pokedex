import shlex
import subprocess
from pathlib import Path

from loguru import logger

from ..util.constants import DATA_OUTPUT_DIR, SPIDER, TYPES_DIR


def run() -> None:
    cmd = shlex.split(
        f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath('pep').with_suffix('.jsonl')} {SPIDER}"
    )
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd, cwd=Path(__file__).parents[1])


def types() -> None:
    logger.info(f"Deleting existing stubs folder: {TYPES_DIR}")
    subprocess.check_output(shlex.split(f"rm -rf src/scrapy_pokedex/{TYPES_DIR}"))

    cmd = shlex.split(f"stubgen -p scrapy_pokedex -o src/scrapy_pokedex/{TYPES_DIR}")
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)


def precommit() -> None:
    logger.info("Running pre-commit hooks")
    cmd = shlex.split("pre-commit run --all-files")
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)


def setup_precommit() -> None:
    logger.info("Setting up pre-commit hooks")
    cmd = shlex.split("pre-commit install")
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)

    logger.info("Updating pre-commit hooks")
    cmd = shlex.split("pre-commit autoupdate")
    logger.info(f"Running: {cmd}")
    subprocess.run(cmd)
