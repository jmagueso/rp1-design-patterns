from adapter.modern_json_reader import ModernJSONReader
from adapter.legacy_csv_reader import LegacyCSVReader
from adapter.csv_to_json_adapter import CSVToJsonAdapter
from adapter.machine_learning_pipeline import MachineLearningPipeline

if __name__ == "__main__":
    print("=== Pipeline com Fonte de Dados Moderna ===")
    json_source = ModernJSONReader("https://api.empresa.com/vendas")
    pipeline_moderno = MachineLearningPipeline(json_source)
    pipeline_moderno.ingest_data()

    print("\n=== Pipeline com Fonte de Dados Legada (Usando Adapter) ===")
    legacy_source = LegacyCSVReader("vendas_2020.csv")
    adapter = CSVToJsonAdapter(legacy_source)
    pipeline_legado = MachineLearningPipeline(adapter)
    
    try:
        pipeline_legado.ingest_data()
    except TypeError:
        print("[Aviso] O CSVToJsonAdapter ainda não foi implementado. Ele retornou None em vez de uma lista.")