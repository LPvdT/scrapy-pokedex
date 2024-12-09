from pathlib import Path

# Paths
DATA_DIR = Path(__package__).with_suffix("") / "data"
DATA_OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = DATA_DIR / "logs"
TYPES_DIR = "typings"

# Spider name
SPIDER = "pokedex_list"

# Max rows to scrape
MAX_ROWS: int = 1000

# Output
filename = f"pokedex_{MAX_ROWS}" if MAX_ROWS is not None else "pokedex"
default_format_ext = ".csv"
OUTPUT_PATH = DATA_OUTPUT_DIR.joinpath(filename)

# Commands for command_factory
COMMANDS = {
    "scrape": f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath(filename).with_suffix(default_format_ext)} {SPIDER}",
    "gen_types": f"stubgen -p scrapy_pokedex -o src/scrapy_pokedex/{TYPES_DIR}",
    "setup_precommit": ["pre-commit install", "pre-commit autoupdate"],
    "precommit": "pre-commit run --all-files",
}
