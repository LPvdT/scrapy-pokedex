from typing import Any, Generator

import scrapy
from scrapy.http import Response

from scrapy_pokedex.items import PokedexItem


class PokedexListSpider(scrapy.Spider):
    name = "pokedex_list"
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/pokedex/all"]

    item = PokedexItem()

    table_xpath = '//*[@id="pokedex"]'
    table_rows = "//tbody/tr"

    queries = {
        "icon_url": {
            "type": "css",
            "selector": "td:nth-child(1) picture img::attr(src)",
        },
        "number": {
            "type": "css",
            "selector": "td:nth-child(1) span::text",
        },
        "name": {
            "type": "css",
            "selector": "td:nth-child(2) a::text",
        },
        "types": {
            "type": "xpath",
            "selector": "td[3]/a/text()",  # This may yield a list of types
        },
        "total": {
            "type": "css",
            "selector": "td:nth-child(4)::text",
        },
        "hp": {
            "type": "css",
            "selector": "td:nth-child(5)::text",
        },
        "attack": {
            "type": "css",
            "selector": "td:nth-child(6)::text",
        },
        "defense": {
            "type": "css",
            "selector": "td:nth-child(7)::text",
        },
        "sp_atk": {
            "type": "css",
            "selector": "td:nth-child(8)::text",
        },
        "sp_def": {
            "type": "css",
            "selector": "td:nth-child(9)::text",
        },
        "speed": {
            "type": "css",
            "selector": "td:nth-child(10)::text",
        },
    }

    def parse(self, response: Response) -> Generator[PokedexItem, Any, None]:
        table = response.xpath(self.table_xpath)
        rows = table.xpath(self.table_rows)

        # DEBUG
        MAX_ROWS: int = 10

        for row in rows[:MAX_ROWS]:
            for key, query in self.queries.items():
                match query.get("type"):
                    case "xpath":
                        entry_xpath = row.xpath(query["selector"]).getall()
                        self.item[key] = entry_xpath
                    case "css":
                        entry_css = row.css(query["selector"]).get()
                        self.item[key] = entry_css
                    case _:
                        raise ValueError(f"Unknown query type: {query['type']}")

            yield self.item
