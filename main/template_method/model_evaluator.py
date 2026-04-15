from abc import ABC, abstractmethod

class ModelEvaluator(ABC):
    
    # Template Method: Define o fluxo de execução que não deve ser alterado
    def evaluate(self, y_true: list, y_pred: list) -> float:
        self._split_data()
        self._train_model()
        self._predict()
        
        metric_result = self.calculate_metrics(y_true, y_pred)
        print(f"Passo 4: Métricas calculadas. Resultado: {metric_result}")
        
        return metric_result

    def _split_data(self):
        print("Passo 1: Dividindo os dados em treino e teste (Simulado)...")

    def _train_model(self):
        print("Passo 2: Treinando o modelo (Simulado)...")

    def _predict(self):
        print("Passo 3: Realizando predições nos dados de teste (Simulado)...")

    @abstractmethod
    def calculate_metrics(self, y_true: list, y_pred: list) -> float:
        """
        Método que deve ser implementado pelas subclasses para 
        calcular a métrica específica do tipo de modelo.
        """
        pass