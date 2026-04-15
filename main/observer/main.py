from observer.model_trainer import ModelTrainer
from observer.observers_concretos import ConsoleLogger, MetricsDashboard
import time

if __name__ == "__main__":
    print("=== Monitoramento de Treinamento de Modelo ML ===\n")

    trainer = ModelTrainer()

    logger = ConsoleLogger()
    dashboard = MetricsDashboard()

    trainer.add(logger)
    trainer.add(dashboard)

    metricas_simuladas = [
        (1, 0.55), (2, 0.72), (3, 0.88), (4, 0.94), (5, 0.98)
    ]

    print("Iniciando treinamento...\n")
    for epoca, acuracia in metricas_simuladas:
        time.sleep(0.5)
        trainer.set_metrics(epoca, acuracia)
        print("-" * 30)

    print("\nTreinamento concluído com sucesso.")