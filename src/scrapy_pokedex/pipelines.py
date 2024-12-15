# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from io import BytesIO
from typing import Type, TypeVar

from itemadapter import ItemAdapter
from scrapy.exporters import BaseItemExporter, JsonItemExporter, JsonLinesItemExporter

from scrapy_pokedex.util.constants import OUTPUT_PATH

from .items import PokedexItem

T = TypeVar("T", bound=BaseItemExporter)


class ScrapyPokedexPipeline:
    def open_spider(self, _) -> None:
        def initialize_exporter(file: BytesIO, exporter_class: Type[T]) -> T:
            exporter = exporter_class(
                file=file, export_empty_fields=True, indent=2, encoding="utf-8"
            )
            exporter.start_exporting()

            return exporter

        # JSONL init
        self.file_jsonl = BytesIO()
        self.exporter_jsonl = initialize_exporter(
            self.file_jsonl, JsonLinesItemExporter
        )

        # JSON init
        self.file_json = BytesIO()
        self.exporter_json = initialize_exporter(self.file_json, JsonItemExporter)

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
        entry = ItemAdapter(item).item

        self.exporter_jsonl.export_item(entry)
        self.exporter_json.export_item(entry)

        return item
