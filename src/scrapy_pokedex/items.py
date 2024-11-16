# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokedexItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    type_1 = scrapy.Field()
    type_2 = scrapy.Field()
