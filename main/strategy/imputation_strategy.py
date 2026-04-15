from abc import ABC, abstractmethod
from typing import List, Optional

class ImputationStrategy(ABC):
    @abstractmethod
    def impute(self, data: List[Optional[float]]) -> List[float]:
        pass