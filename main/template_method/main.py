from template_method.evaluators import ClassificationEvaluator, RegressionEvaluator

if __name__ == "__main__":
    print("Iniciando o pipeline de avaliação de modelos...\n")

    print("=== Avaliação do Modelo de Classificação ===")
    
    # Dados simulados (Ex: 1 = Fraude, 0 = Transação Normal)
    y_true_class = [1, 0, 1, 1, 0]
    y_pred_class = [1, 0, 0, 1, 0]

    try:
        class_evaluator = ClassificationEvaluator()
        class_evaluator.evaluate(y_true_class, y_pred_class)
    except NotImplementedError:
        print("[Aviso] O ClassificationEvaluator ainda não foi implementado.")

    print("\n" + "="*50 + "\n")

    print("=== Avaliação do Modelo de Regressão ===")
    
    # Dados simulados (Ex: Previsão de preços de casas em milhares)
    y_true_reg = [300.0, 250.5, 420.0, 700.0]
    y_pred_reg = [290.5, 250.0, 420.0, 800.0]

    try:
        reg_evaluator = RegressionEvaluator()
        reg_evaluator.evaluate(y_true_reg, y_pred_reg)
    except NotImplementedError:
        print("[Aviso] O RegressionEvaluator ainda não foi implementado.")