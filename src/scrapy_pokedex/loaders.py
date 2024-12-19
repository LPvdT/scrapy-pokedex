from urllib.parse import urlparse

from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from .items import PokedexItem


def _is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def _to_int(value: str) -> int:
    return int(value.lstrip("0"))


class PokedexLoader(ItemLoader):
    default_item_class = PokedexItem

    to_int = Compose(MapCompose(_to_int), TakeFirst())
    to_url = Compose(MapCompose(lambda v: v if _is_valid_url(v) else None), TakeFirst())

    FIELDS_TO_INT = [
        "total",
        "hp",
        "attack",
        "defense",
        "sp_atk",
        "sp_def",
        "speed",
    ]

    # Output processors
    icon_url_out = to_url
    number_out = to_int
    name_out = Compose(MapCompose(lambda v: v.strip()), TakeFirst())
    name_alt_out = Compose(MapCompose(lambda v: v.strip()), TakeFirst())
    types_out = MapCompose(lambda v: v.strip())

    for field in FIELDS_TO_INT:
        locals()[f"{field}_out"] = to_int
