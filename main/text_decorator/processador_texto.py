from abc import ABC, abstractmethod

class ProcessadorTexto(ABC):
    @abstractmethod
    def processarTexto(self, texto: str) -> str:
        pass

    @abstractmethod
    def tempoEstimadoProcessamento(self, palavras: int) -> float:
        pass