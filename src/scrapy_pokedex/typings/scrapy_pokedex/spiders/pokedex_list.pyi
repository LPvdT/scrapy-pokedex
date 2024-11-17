import scrapy
from ..items import PokedexItem as PokedexItem
from _typeshed import Incomplete
from scrapy.http import Response as Response

class PokedexListSpider(scrapy.Spider):
    name: str
    allowed_domains: Incomplete
    start_urls: Incomplete
    item: Incomplete
    queries: Incomplete
    def parse(self, response: Response): ...
