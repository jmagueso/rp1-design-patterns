from adapter.json_data_source import JSONDataSource
from typing import List, Dict

class ModernJSONReader(JSONDataSource):
    def __init__(self, api_endpoint: str):
        self.api_endpoint = api_endpoint

    def get_json_records(self) -> List[Dict[str, str]]:
        print(f"Extraindo dados JSON nativos de {self.api_endpoint}")
        return [{"id": "1", "produto": "Teclado", "vendas": "150"}]