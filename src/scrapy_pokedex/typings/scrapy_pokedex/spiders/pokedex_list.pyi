import scrapy
from _typeshed import Incomplete
from scrapy.http import Response as Response
from scrapy_pokedex.items import PokedexItem as PokedexItem
from scrapy_pokedex.loaders import PokedexLoader as PokedexLoader
from scrapy_pokedex.settings import MAX_ROWS as MAX_ROWS, SPIDER as SPIDER
from typing import Any, Generator

class PokedexListSpider(scrapy.Spider):
    name = SPIDER
    allowed_domains: Incomplete
    start_urls: Incomplete
    table_xpath: str
    table_rows: str
    def parse(self, response: Response) -> Generator[PokedexItem, Any, None]: ...
