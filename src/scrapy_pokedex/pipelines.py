# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from io import BytesIO

from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter

from scrapy_pokedex.util.constants import OUTPUT_PATH

from .items import PokedexItem


class ScrapyPokedexPipeline:
    def open_spider(self, _) -> None:
        # JSONL init
        self.file_jsonl = BytesIO()
        self.exporter_jsonl = JsonLinesItemExporter(self.file_jsonl)
        self.exporter_jsonl.start_exporting()

        # JSON init
        self.file_json = BytesIO()
        self.exporter_json = JsonItemExporter(self.file_json)
        self.exporter_json.start_exporting()

    def close_spider(self, _) -> None:
        # JSONL finish
        self.exporter_jsonl.finish_exporting()
        with open(OUTPUT_PATH.with_suffix(".jsonl"), "wb") as f:
            f.write(self.file_jsonl.getvalue())

        # JSON finish
        self.exporter_json.finish_exporting()
        with open(OUTPUT_PATH.with_suffix(".json"), "wb") as f:
            f.write(self.file_json.getvalue())

    def process_item(self, item: PokedexItem, _) -> PokedexItem:
        entry = ItemAdapter(item).asdict()

        self.exporter_jsonl.export_item(entry)
        self.exporter_json.export_item(entry)

        return item
