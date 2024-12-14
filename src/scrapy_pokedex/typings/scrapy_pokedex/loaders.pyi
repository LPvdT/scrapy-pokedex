from .items import PokedexItem as PokedexItem
from _typeshed import Incomplete
from scrapy.loader import ItemLoader

class PokedexLoader(ItemLoader):
    default_item_class = PokedexItem
    to_int: Incomplete
    FIELDS_TO_INT: Incomplete
    icon_url_out: Incomplete
    number_out = to_int
    name_out: Incomplete
    name_alt_out: Incomplete
    types_out: Incomplete
