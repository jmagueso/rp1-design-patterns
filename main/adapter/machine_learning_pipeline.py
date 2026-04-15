from adapter.json_data_source import JSONDataSource

class MachineLearningPipeline:
    def __init__(self, data_source: JSONDataSource):
        self.data_source = data_source

    def ingest_data(self):
        # O pipeline SÓ sabe lidar com get_json_records!
        data = self.data_source.get_json_records()
        print(f"Dados ingeridos no pipeline: {data}")