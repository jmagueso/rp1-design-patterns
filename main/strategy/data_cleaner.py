from typing import List, Optional

class DataCleaner:

    # FIXME só aceita um tipo de imputação (preenchendo com zeros)
    def clean_column(self, data: List[Optional[float]]) -> List[float]:
        return [0.0 if x is None else x for x in data]