from observer.observer import Observer
from observer.model_trainer import ModelTrainer

class ConsoleLogger(Observer):
    def update(self, subject: ModelTrainer) -> None:
        print(f"[Log] Época {subject.get_epoch()} concluída. Acurácia: {subject.get_accuracy():.2f}")

class MetricsDashboard(Observer):
    def update(self, subject: ModelTrainer) -> None:
        # Imprime simulando a atualização de um gráfico (convertendo para porcentagem)
        print(f"[Dashboard] Atualizando gráfico -> Acurácia: {subject.get_accuracy() * 100:.1f}% na época {subject.get_epoch()}")