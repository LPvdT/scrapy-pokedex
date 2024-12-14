from .items import PokedexItem as PokedexItem
from _typeshed import Incomplete
from scrapy_pokedex.util.constants import OUTPUT_PATH as OUTPUT_PATH

class ScrapyPokedexPipeline:
    file_jsonl: Incomplete
    exporter_jsonl: Incomplete
    file_json: Incomplete
    exporter_json: Incomplete
    def open_spider(self, _) -> None: ...
    def close_spider(self, _) -> None: ...
    def process_item(self, item: PokedexItem, _) -> PokedexItem: ...
