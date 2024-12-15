# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokedexItem(scrapy.Item):
    # Image pipeline fields
    image_urls = scrapy.Field()
    images = scrapy.Field()

    # Regular fields
    icon_url = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    name_alt = scrapy.Field()
    types = scrapy.Field()
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_atk = scrapy.Field()
    sp_def = scrapy.Field()
    speed = scrapy.Field()
