from template_method.model_evaluator import ModelEvaluator

class ClassificationEvaluator(ModelEvaluator):
    # TODO: Implemente o método calculate_metrics herdado.
    # A métrica deve ser a Acurácia (Accuracy): 
    # (Quantidade de acertos) / (Total de amostras)
    pass


class RegressionEvaluator(ModelEvaluator):
    # TODO: Implemente o método calculate_metrics herdado.
    # A métrica deve ser o Erro Quadrático Médio (MSE): 
    # Soma dos quadrados das diferenças entre y_true e y_pred, dividida pelo total de amostras.
    pass