import unittest
from singleton.db_connection import DataLakeConnection as DBConnection

class SingletonTest(unittest.TestCase):
    
    def setUp(self):
        DBConnection._instance = None

    def test_no_public_constructor(self):
        """Construtor deve ser bloqueado para novas instâncias (simulando construtor privado)"""
        DBConnection.get_instance("jdbc:as400://myiSeries;proxy server=myHODServer:3470")
        
        with self.assertRaises(Exception):
            DBConnection("jdbc:as400://myiSeries;proxy server=myHODServer:3470")

    def test_has_get_instance(self):
        """Deve possuir método get_instance"""
        self.assertTrue(hasattr(DBConnection, "get_instance"), "A classe não possui o método get_instance")
        self.assertTrue(callable(getattr(DBConnection, "get_instance")), "get_instance deve ser um método/função")

    def test_has_same_instance(self):
        """Duas instâncias distintas devem ser iguais"""
        db1 = DBConnection.get_instance("jdbc:as400://myiSeries;proxy server=myHODServer:3470")
        db2 = DBConnection.get_instance("jdbc:as400://myiSeries;proxy server=myHODServer:3470")

        # assertIs verifica se ambas as variáveis apontam para o mesmo objeto na memória
        self.assertIs(db1, db2, "As instâncias retornadas não são as mesmas")

if __name__ == '__main__':
    unittest.main()