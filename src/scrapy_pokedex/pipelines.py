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
from .settings import BATCH_SIZE

T = TypeVar("T", bound=BaseItemExporter)


class ScrapyPokedexPipeline:
    def __init__(self) -> None:
        self.buffer: list[PokedexItem] = []
        self.batch_size = BATCH_SIZE if BATCH_SIZE is not None else 250
        self.batch_count: int = 1

        self.file_jsonl: BytesIO
        self.file_json: BytesIO

    def _initialize_exporter(self, file: BytesIO, exporter_class: Type[T]) -> T:
        exporter = exporter_class(
            file=file, export_empty_fields=True, indent=2, encoding="utf-8"
        )
        exporter.start_exporting()

        return exporter

    def _flush_buffer(self) -> None:
        # JSONL exporter
        self.file_jsonl = BytesIO()
        self.exporter_jsonl = self._initialize_exporter(
            self.file_jsonl, JsonLinesItemExporter
        )

        # JSON exporter
        self.file_json = BytesIO()
        self.exporter_json = self._initialize_exporter(self.file_json, JsonItemExporter)

        # Export items
        for item in self.buffer:
            self.exporter_jsonl.export_item(item)
            self.exporter_json.export_item(item)

        # JSONL finish
        self.exporter_jsonl.finish_exporting()

        output_jsonl = OUTPUT_PATH.with_name(
            f"{OUTPUT_PATH.name}_{self.batch_size}_{self.batch_count}"
        ).with_suffix(".jsonl")
        with open(output_jsonl, "wb") as f:
            f.write(self.file_jsonl.getvalue())

        # JSON finish
        self.exporter_json.finish_exporting()
        output_json = OUTPUT_PATH.with_name(
            f"{OUTPUT_PATH.name}_{self.batch_size}_{self.batch_count}"
        ).with_suffix(".json")
        with open(output_json, "wb") as f:
            f.write(self.file_json.getvalue())

        # Clear buffer
        self.buffer = []
        self.batch_count += 1

    def process_item(self, item: PokedexItem, _) -> PokedexItem:
        entry = ItemAdapter(item).item
        self.buffer.append(entry)

        if len(self.buffer) >= self.batch_size:
            self._flush_buffer()

        return item

    def open_spider(self, _) -> None:
        pass

    def close_spider(self, _) -> None:
        if len(self.buffer) > 0:
            self._flush_buffer()
