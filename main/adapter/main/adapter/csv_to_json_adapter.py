from adapter.json_data_source import JSONDataSource
from adapter.legacy_csv_reader import LegacyCSVReader
from typing import List, Dict

class CSVToJsonAdapter(JSONDataSource):
    def __init__(self, legacy_reader: LegacyCSVReader):
        self.legacy_reader = legacy_reader

    def get_json_records(self) -> List[Dict[str, str]]:
        # TODO: Implemente a adaptação aqui.
        # 1. Chame o método read_csv_lines() do legacy_reader.
        # 2. Converta a lista de strings CSV em uma lista de dicionários.
        # 3. Retorne essa lista.
        pass
