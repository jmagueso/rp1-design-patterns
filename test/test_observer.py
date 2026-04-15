import unittest
import io
import sys
from observer.model_trainer import ModelTrainer
from observer.observers_concretos import ConsoleLogger, MetricsDashboard

class ObserverTest(unittest.TestCase):

    def test_observers_are_added(self):
        """Observers devem ser adicionados na lista interna do Sujeito"""
        trainer = ModelTrainer()
        trainer.add(ConsoleLogger())
        trainer.add(MetricsDashboard())

        observers = getattr(trainer, "_observers")
        
        self.assertEqual(2, len(observers), "A lista de observadores não contém os 2 elementos adicionados.")

    def test_observers_are_notified(self):
        """Observers devem ser notificados e gerar as saídas corretas"""
        trainer = ModelTrainer()
        trainer.add(ConsoleLogger())
        trainer.add(MetricsDashboard())

        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            trainer.set_metrics(1, 0.85)
        finally:
            sys.stdout = sys.__stdout__

        saida_console = captured_output.getvalue()

        self.assertIn("[Log] Época 1 concluída. Acurácia: 0.85", saida_console)
        self.assertIn("[Dashboard] Atualizando gráfico -> Acurácia: 85.0% na época 1", saida_console)

if __name__ == '__main__':
    unittest.main()