from text_decorator.processador_decorator import ProcessadorDecorator

class TextoBase(ProcessadorDecorator):
    def __init__(self, processador=None):
        super().__init__(processador)

    def processarTexto(self, texto: str) -> str:
        # Apenas repassa para a cadeia (se houver) ou retorna o texto puro
        if self._processador is not None:
            return self._processador.processarTexto(texto)
        return texto

    def tempoEstimadoProcessamento(self, palavras: int) -> float:
        custo = 0.0
        if self._processador is not None:
            custo += self._processador.tempoEstimadoProcessamento(palavras)
        return custo