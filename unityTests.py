import os
import unittest

from faker import Faker

from database.config.config import config
from database.populateDatabase import (populateAssociado, populateCartao,
                                       populateConta, populateMovimento)


class TestClass(unittest.TestCase):
    
    def test_config_database(self):
        filename = "database.ini"
        section = "postgresql"
        self.assertNotEqual(config(filename, section), 'Section {0} not found in the {1} file'.format(section, filename))
        
    def test_populate_associado(self):
        fake = Faker()
        self.assertTrue(populateAssociado(fake, 1))
        
    def test_populate_conta(self):
        self.assertTrue(populateConta())
        
    def test_populate_cartao(self):
        fake = Faker()
        self.assertTrue(populateCartao(fake, 1))
        
    def test_populate_movimento(self):
        fake = Faker()
        self.assertTrue(populateMovimento(fake, 1))        
        
if __name__ == "__main__":
    unittest.main()
