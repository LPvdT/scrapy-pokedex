from pathlib import Path

# Paths
DATA_DIR = Path(__file__).parent / "data"
DATA_OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = DATA_DIR / "logs"
TYPES_DIR = "typings"

# Spider name
SPIDER = "pokedex_list"

# Commands for command_factory
COMMANDS = {
    "scrape": f"scrapy crawl -O {DATA_OUTPUT_DIR.joinpath('pep').with_suffix('.jsonl')} {SPIDER}",
    "gen_types": f"stubgen -p scrapy_pokedex -o src/scrapy_pokedex/{TYPES_DIR}",
    "setup_precommit": ["pre-commit install", "pre-commit autoupdate"],
    "precommit": "pre-commit run --all-files",
}
