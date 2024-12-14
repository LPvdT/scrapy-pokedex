from pathlib import Path

# Config
# TODO: Move to YAML config file
ENABLE_DEBUG: bool = False
MAX_ROWS: int | None = None
DEFAULT_OUTPUT: bool = False

# Paths
DATA_DIR = Path(__package__).with_suffix("") / "data"
DATA_OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = DATA_DIR / "logs"
TYPES_DIR = "typings"

# Spider name
SPIDER = "pokedex_list"
JOB_DIR = DATA_DIR / "crawls" / f"{SPIDER}-1"

# Output
filename = f"pokedex_{MAX_ROWS}" if MAX_ROWS is not None else "pokedex"
default_format_ext = ".csv"
OUTPUT_PATH = DATA_OUTPUT_DIR.joinpath(filename)
DEFAULT_OUTPUT_URI = (
    f"-O {DATA_OUTPUT_DIR.joinpath(filename).with_suffix(default_format_ext)}"
)

# Commands for command_factory
COMMANDS = {
    "scrape": f"scrapy crawl {DEFAULT_OUTPUT if DEFAULT_OUTPUT else ''} {SPIDER} -s JOBDIR={JOB_DIR}",
    "gen_types": f"stubgen -p scrapy_pokedex -o src/scrapy_pokedex/{TYPES_DIR}",
    "setup_precommit": ["pre-commit install", "pre-commit autoupdate"],
    "precommit": "pre-commit run --all-files",
}
