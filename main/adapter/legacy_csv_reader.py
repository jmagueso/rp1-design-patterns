from typing import List

class LegacyCSVReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_csv_lines(self) -> List[str]:
        print(f"Lendo arquivo legado CSV: {self.filename}")
        return [
            "id,produto,vendas",
            "2,Mouse,200",
            "3,Monitor,50"
        ]