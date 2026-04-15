import unittest
import importlib

class StrategyTest(unittest.TestCase):

    def setUp(self):
        try:
            modulo_strategies = importlib.import_module("strategy.strategies")
            self.zero_class = getattr(modulo_strategies, "ZeroImputationStrategy")
            self.mean_class = getattr(modulo_strategies, "MeanImputationStrategy")
            self.median_class = getattr(modulo_strategies, "MedianImputationStrategy")
            
            modulo_cleaner = importlib.import_module("strategy.data_cleaner")
            self.cleaner_class = getattr(modulo_cleaner, "DataCleaner")
            
        except (ImportError, AttributeError) as e:
            self.fail(f"Erro de Reflexão/Importação: {e}. Crie as classes no arquivo strategy/strategies.py e DataCleaner em data_cleaner.py")

        self.zero_strategy = self.zero_class()
        self.mean_strategy = self.mean_class()
        self.median_strategy = self.median_class()

    def test_should_impute_with_zero(self):
        """Estratégia Zero deve substituir None por 0.0"""
        impute_method = getattr(self.zero_strategy, "impute")
        self.assertEqual(impute_method([10.0, None, 20.0]), [10.0, 0.0, 20.0])

    def test_should_impute_with_mean(self):
        """Estratégia Mean deve substituir None pela média"""
        impute_method = getattr(self.mean_strategy, "impute")
        self.assertEqual(impute_method([10.0, None, 20.0]), [10.0, 15.0, 20.0])

    def test_should_impute_with_median(self):
        """Estratégia Median deve substituir None pela mediana"""
        impute_method = getattr(self.median_strategy, "impute")
        self.assertEqual(impute_method([10.0, None, 20.0, 100.0]), [10.0, 20.0, 20.0, 100.0])

    def test_should_verify_all_strategies(self):
        """Strategies devem ser verificadas no DataCleaner (Contexto)"""
        cleaner = self.cleaner_class()
        
        self.assertTrue(hasattr(cleaner, "setStrategy"), "DataCleaner deve possuir o método setStrategy")
        self.assertTrue(hasattr(cleaner, "clean_column"), "DataCleaner deve possuir o método clean_column")
        
        set_strategy = getattr(cleaner, "setStrategy")
        clean_column = getattr(cleaner, "clean_column")

        set_strategy(self.zero_strategy)
        self.assertEqual(clean_column([None, 10.0]), [0.0, 10.0])

        set_strategy(self.mean_strategy)
        self.assertEqual(clean_column([None, 10.0]), [10.0, 10.0])

        set_strategy(self.median_strategy)
        self.assertEqual(clean_column([None, 10.0]), [10.0, 10.0])

if __name__ == '__main__':
    unittest.main()