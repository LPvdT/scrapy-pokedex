from typing import Any, Generator

import scrapy
from scrapy.http import Response

from scrapy_pokedex.items import PokedexItem
from scrapy_pokedex.loaders import PokedexLoader
from scrapy_pokedex.settings import MAX_ROWS, SPIDER


class PokedexListSpider(scrapy.Spider):
    name = SPIDER
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/pokedex/all"]

    table_xpath = '//*[@id="pokedex"]'
    table_rows = "//tbody/tr"

    def parse(self, response: Response) -> Generator[PokedexItem, Any, None]:
        table = response.xpath(self.table_xpath)
        rows = table.xpath(self.table_rows)

        for row in rows[:MAX_ROWS]:
            loader = PokedexLoader(selector=row)

            loader.add_css("icon_url", "td:nth-child(1) picture img::attr(src)")
            loader.add_css("number", "td:nth-child(1) span::text")
            loader.add_css("name", "td:nth-child(2) a::text")
            loader.add_css("name_alt", "td:nth-child(2) small::text")
            loader.add_xpath("types", "td[3]/a/text()")
            loader.add_css("total", "td:nth-child(4)::text")
            loader.add_css("hp", "td:nth-child(5)::text")
            loader.add_css("attack", "td:nth-child(6)::text")
            loader.add_css("defense", "td:nth-child(7)::text")
            loader.add_css("sp_atk", "td:nth-child(8)::text")
            loader.add_css("sp_def", "td:nth-child(9)::text")
            loader.add_css("speed", "td:nth-child(10)::text")

            yield loader.load_item()
