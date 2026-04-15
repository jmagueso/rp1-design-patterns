import unittest
import io
import sys
from adapter.modern_json_reader import ModernJSONReader
from adapter.legacy_csv_reader import LegacyCSVReader
from adapter.csv_to_json_adapter import CSVToJsonAdapter
from adapter.machine_learning_pipeline import MachineLearningPipeline

class AdapterTest(unittest.TestCase):

    def setUp(self):
        self.json_nativo = ModernJSONReader("fake_api")
        self.legado_csv = LegacyCSVReader("fake.csv")
        self.adapter = CSVToJsonAdapter(self.legado_csv)
        self.out_content = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.out_content

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_native_json_ingestion(self):
        """Testa se o pipeline funciona com a fonte de dados moderna (JSON nativo)"""
        pipeline = MachineLearningPipeline(self.json_nativo)
        pipeline.ingest_data()
        saida = self.out_content.getvalue()
        
        self.assertIn("Teclado", saida)

    def test_adapter_has_get_json_records_method(self):
        """Verifica se a classe Adapter implementou o método obrigatório da interface"""
        self.assertTrue(hasattr(CSVToJsonAdapter, "get_json_records"), 
                        "A classe CSVToJsonAdapter deve ter o método get_json_records()")

    def test_adapter_translation(self):
        """Testa se o Adapter traduziu o CSV para a estrutura correta (Lista de Dicionários)"""
        resultado = self.adapter.get_json_records()
        
        self.assertIsInstance(resultado, list, "O Adapter deve retornar uma lista.")
        
        # A lista deve conter dicionários
        if len(resultado) > 0:
            self.assertIsInstance(resultado[0], dict, "Os elementos da lista devem ser dicionários.")
            
        # O CSV possui 2 linhas de dados (Mouse e Monitor). O cabeçalho não conta como dado.
        self.assertEqual(2, len(resultado))
        
        # Verifica se o mapeamento Chave-Valor ocorreu corretamente no primeiro elemento
        self.assertEqual("2", resultado[0].get("id"))
        self.assertEqual("Mouse", resultado[0].get("produto"))
        self.assertEqual("200", resultado[0].get("vendas"))

    def test_pipeline_with_adapter_ingestion(self):
        """Testa se o pipeline de ML consegue ingerir os dados consumindo através do Adapter"""
        pipeline = MachineLearningPipeline(self.adapter)
        pipeline.ingest_data()
        saida = self.out_content.getvalue()
        
        # O print do legacy_reader e do pipeline devem constar no console
        self.assertTrue("Lendo arquivo legado CSV:" in saida)
        self.assertTrue("Mouse" in saida)
        self.assertTrue("Monitor" in saida)

if __name__ == '__main__':
    unittest.main()
