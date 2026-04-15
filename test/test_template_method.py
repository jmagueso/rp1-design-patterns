import unittest
import importlib
from template_method.model_evaluator import ModelEvaluator

class TemplateMethodTest(unittest.TestCase):

    def setUp(self):
        try:
            modulo = importlib.import_module("template_method.evaluators")
            self.classificacao_class = getattr(modulo, "ClassificationEvaluator")
            self.regressao_class = getattr(modulo, "RegressionEvaluator")
        except (ImportError, AttributeError) as e:
            self.fail(f"Erro ao carregar as classes. Certifique-se de criá-las em evaluators.py: {e}")

    def test_has_calculate_metrics_method(self):
        """Verifica se o método obrigatório calculate_metrics foi implementado"""
        self.assertTrue(issubclass(self.classificacao_class, ModelEvaluator))
        self.assertTrue(issubclass(self.regressao_class, ModelEvaluator))
        
        self.assertTrue(hasattr(self.classificacao_class, "calculate_metrics"))
        self.assertTrue(hasattr(self.regressao_class, "calculate_metrics"))

    def test_classification_accuracy(self):
        """Verifica o fluxo completo de avaliação e a matemática da Acurácia"""
        avaliador = self.classificacao_class()
        y_true = [1, 0, 1, 1, 0]
        y_pred = [1, 0, 0, 1, 0] 

        resultado = avaliador.evaluate(y_true, y_pred)
        
        self.assertEqual(0.8, resultado, "O cálculo de Acurácia está incorreto.")

    def test_regression_mse(self):
        """Verifica o fluxo completo de avaliação e a matemática do MSE"""
        avaliador = self.regressao_class()
        y_true = [3.0, -0.5, 2.0, 7.0]
        y_pred = [2.5,  0.0, 2.0, 8.0]
        
        # Erros:
        # (3.0 - 2.5)^2 = 0.25
        # (-0.5 - 0.0)^2 = 0.25
        # (2.0 - 2.0)^2 = 0.00
        # (7.0 - 8.0)^2 = 1.00
        # Soma = 1.50 -> Dividido por 4 = 0.375
        
        resultado = avaliador.evaluate(y_true, y_pred)
        
        self.assertEqual(0.375, resultado, "O cálculo do Erro Quadrático Médio (MSE) está incorreto.")

if __name__ == '__main__':
    unittest.main()