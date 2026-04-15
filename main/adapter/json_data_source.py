from abc import ABC, abstractmethod
from typing import List, Dict

class JSONDataSource(ABC):
    @abstractmethod
    def get_json_records(self) -> List[Dict[str, str]]:
        """Retorna uma lista de dicionários simulando um JSON"""
        pass