import scrapy


class PokedexListSpider(scrapy.Spider):
    name = "pokedex_list"
    allowed_domains = ["pokemon.fandom.com"]
    start_urls = ["https://pokemon.fandom.com/wiki/List_of_Pokémon"]

    def parse(self, response):
        pass
