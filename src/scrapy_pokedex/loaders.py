from urllib.parse import urlparse

from itemloaders.processors import Compose, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from .items import PokedexItem


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


to_int = Compose(TakeFirst(), int)


class PokedexLoader(ItemLoader):
    default_item_class = PokedexItem

    # Output processors
    icon_url_out = Compose(
        MapCompose(lambda v: v if is_valid_url(v) else None), TakeFirst()
    )
    number_out = Compose(
        MapCompose(lambda v: v.lstrip("0"), lambda v: int(v)), TakeFirst()
    )
    name_out = Compose(MapCompose(lambda v: v.strip()), TakeFirst())
    name_alt_out = Compose(
        MapCompose(lambda v: v.strip() if v is not None else ""), TakeFirst()
    )
    types_out = MapCompose(lambda v: v.strip())
    total_out = to_int
    hp_out = to_int
    attack_out = to_int
    defense_out = to_int
    sp_atk_out = to_int
    sp_def_out = to_int
    speed_out = to_int
