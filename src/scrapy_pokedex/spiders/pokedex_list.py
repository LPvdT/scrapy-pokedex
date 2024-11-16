import scrapy

from ..items import PokedexItem


class PokedexListSpider(scrapy.Spider):
    name = "pokedex_list"
    allowed_domains = ["pokemon.fandom.com"]
    start_urls = ["https://pokemon.fandom.com/wiki/List_of_Pokémon"]
    item = PokedexItem()

    queries = {
        "number": "td:nth-child(1)::text",
        "name": "td:nth-child(3) a::text",
        "type_1": "td:nth-child(4) span::text",
        "type_2": "td:nth-child(5) span::text",
    }

    def parse(self, response):
        all_tables = response.css("table.wikitable tr")

        for pokemon in all_tables:
            for key, value in self.queries.items():
                self.item[key] = pokemon.css(value).get()
            yield self.item
