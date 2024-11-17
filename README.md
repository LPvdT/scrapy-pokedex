# Scrapy Pokedex<a name="scrapy-pokedex"></a>

A Scrapy project for scraping Pokémon data.

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [Scrapy Pokedex](#scrapy-pokedex)
  - [To do](#to-do)
  - [Project Structure](#project-structure)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

<!-- mdformat-toc end -->

## To do<a name="to-do"></a>

- [ ] Further implement scraper
  - [ ] Implement pipelines
  - [ ] Implement middleware
  - [ ] Implement proxies
  - [ ] Implement agent headers

## Project Structure<a name="project-structure"></a>

- `src/`: Source code directory
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

## Requirements<a name="requirements"></a>

- [`uv`](https://docs.astral.sh/uv/)

## Installation<a name="installation"></a>

1. Clone the repository: `git clone https://github.com/LPvdT/scrapy-pokedex`
1. Install dependencies: `uv sync --group dev --group test`

## Usage<a name="usage"></a>

1. Run the spider: `uv run scrape`

## Contributing<a name="contributing"></a>

Contributions are welcome! Please submit a pull request with your changes.

## License<a name="license"></a>

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
