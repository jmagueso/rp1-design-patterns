from text_decorator.processador_texto import ProcessadorTexto

class ProcessadorDecorator(ProcessadorTexto):
    def __init__(self, processador: ProcessadorTexto = None):
        self._processador = processador

    def processarTexto(self, texto: str) -> str:
        if self._processador is not None:
            return self._processador.processarTexto(texto)
        return texto

    def tempoEstimadoProcessamento(self, palavras: int) -> float:
        if self._processador is not None:
            return self._processador.tempoEstimadoProcessamento(palavras)
        return 0.0