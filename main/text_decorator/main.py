from text_decorator.texto_base import TextoBase
from text_decorator.filtros import LowerCase, RemovePunctuation, RemoveStopWords, Stemming

if __name__ == "__main__":
    print("=== Sistema de Limpeza de Texto (NLP) ===\n")

    texto_sujo = "Os dados, que sao valiosos, precisam de filtros!"
    print(f"Texto Original: {texto_sujo}\n")

    pipeline_simples = LowerCase(TextoBase())
    print("--- Pipeline: Apenas LowerCase ---")
    print(f"Resultado: {pipeline_simples.processarTexto(texto_sujo)}")
    print(f"Tempo Estimado: {pipeline_simples.tempoEstimadoProcessamento(8)} ms\n")

    pipeline_full = Stemming(
        RemoveStopWords(
            RemovePunctuation(
                LowerCase(TextoBase())
            )
        )
    )

    print("--- Pipeline: Completo (Todos os Filtros) ---")
    print(f"Resultado Final: {pipeline_full.processarTexto(texto_sujo)}")

    print(f"Tempo Estimado Total: {pipeline_full.tempoEstimadoProcessamento(8)} ms")