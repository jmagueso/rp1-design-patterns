import unittest
import importlib
from text_decorator.texto_base import TextoBase

class DecoratorTest(unittest.TestCase):

    def test_has_all_filters(self):
        """Deve ter as quatro classes de filtro"""
        filtros = ['LowerCase', 'RemovePunctuation', 'RemoveStopWords', 'Stemming']
        
        for filtro in filtros:
            try:
                modulo = importlib.import_module("text_decorator.filtros")
                getattr(modulo, filtro)
            except (ImportError, AttributeError):
                self.fail(f"Sem classe {filtro}. Certifique-se de criá-la em text_decorator/filtros.py")

    def test_has_correct_costs(self):
        """Filtros isolados devem ter o custo computacional certo para 1 palavra"""
        modulo = importlib.import_module("text_decorator.filtros")
        
        LowerCase = getattr(modulo, 'LowerCase')
        RemovePunctuation = getattr(modulo, 'RemovePunctuation')
        RemoveStopWords = getattr(modulo, 'RemoveStopWords')
        Stemming = getattr(modulo, 'Stemming')

        self.assertEqual(0.25, LowerCase().tempoEstimadoProcessamento(1))
        self.assertEqual(0.50, RemovePunctuation().tempoEstimadoProcessamento(1))
        self.assertEqual(1.00, RemoveStopWords().tempoEstimadoProcessamento(1))
        self.assertEqual(1.50, Stemming().tempoEstimadoProcessamento(1))

    def test_filters_combination(self):
        """Filtros devem poder ser combinados sequencialmente"""
        modulo = importlib.import_module("text_decorator.filtros")
        
        LowerCase = getattr(modulo, 'LowerCase')
        RemovePunctuation = getattr(modulo, 'RemovePunctuation')
        RemoveStopWords = getattr(modulo, 'RemoveStopWords')
        Stemming = getattr(modulo, 'Stemming')

        base = TextoBase()
        passo1 = LowerCase(base)
        passo2 = RemovePunctuation(passo1)
        passo3 = RemoveStopWords(passo2)
        pipeline_completo = Stemming(passo3)

        texto_original = "Os dados, que sao valiosos!"
        qtd_palavras = 5
        
        self.assertEqual(16.25, pipeline_completo.tempoEstimadoProcessamento(qtd_palavras))
        
        # Testando a transformação da string
        # 1. LowerCase: "os dados, que sao valiosos!"
        # 2. Punctuation: "os dados que sao valiosos"
        # 3. StopWords: "os dados sao valiosos"
        # 4. Stemming: "o dado sao valioso"
        self.assertEqual("o dado sao valioso", pipeline_completo.processarTexto(texto_original))

if __name__ == '__main__':
    unittest.main()