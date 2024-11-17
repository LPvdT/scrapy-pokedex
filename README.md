# Scrapy Pokedex

A Scrapy project for scraping Pokémon data.

## Project Structure

______________________________________________________________________

- src/: Source code directory
  - `scrapy_pokedex/`: Scrapy project directory
    - `items.py`: Defines the data structures for scraped items
    - `middlewares.py`: Custom middleware for the Scrapy project
    - `pipelines.py`: Data processing pipelines for the Scrapy project
    - `settings.py`: Scrapy project settings
    - `spiders/`: Directory for Scrapy spiders
      - `pokedex_list.py`: Spider for scraping Pokémon list data
    - `typings/`: Directory for type annotations
      - `scrapy_pokedex/`: Type annotations for the Scrapy project
    - `util/`: Utility directory
      - `fs.py`: File system utilities
      - `interceptor.py`: Custom interceptor for the Scrapy project
      - `factory.py`: Factory functions for creating objects
      - `constants.py`: Constants used throughout the project

## Requirements

______________________________________________________________________

- [`uv`](https://docs.astral.sh/uv/)

## Installation

______________________________________________________________________

1. Clone the repository: `git clone https://github.com/LPvdT/scrapy-pokedex`
1. Install dependencies: `uv sync --group dev --group test`

## Usage

______________________________________________________________________

1. Run the spider: `uv run scrape`

## Contributing

______________________________________________________________________

Contributions are welcome! Please submit a pull request with your changes.

## License

______________________________________________________________________

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
