from urllib.parse import urlparse

import itemloaders.processors as pc
from scrapy.loader import ItemLoader

from .items import PokedexItem


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


class PokedexLoader(ItemLoader):
    default_item_class = PokedexItem
    default_input_processor = pc.TakeFirst()
    default_output_processor = pc.TakeFirst()

    # Input processors
    types_in = pc.Identity()

    # Output processors
    icon_url_out = pc.MapCompose(lambda v: v if is_valid_url(v) else None)
    number_out = pc.MapCompose(lambda v: v.lstrip("0"), lambda v: int(v))
    name_out = pc.MapCompose(lambda v: v.strip())
    name_alt_out = pc.MapCompose(lambda v: v.strip() if v is not None else None)
    types_out = pc.MapCompose(lambda v: [x.strip() for x in v])
    total_out = pc.MapCompose(lambda v: int(v))
    hp_out = pc.MapCompose(lambda v: int(v))
    attack_out = pc.MapCompose(lambda v: int(v))
    defense_out = pc.MapCompose(lambda v: int(v))
    sp_atk_out = pc.MapCompose(lambda v: int(v))
    sp_def_out = pc.MapCompose(lambda v: int(v))
    speed_out = pc.MapCompose(lambda v: int(v))
