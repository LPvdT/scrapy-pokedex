import scrapy
from _typeshed import Incomplete

class PokedexListSpider(scrapy.Spider):
    name: str
    allowed_domains: Incomplete
    start_urls: Incomplete
    def parse(self, response) -> None: ...
