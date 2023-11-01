import unittest

from ProductionCode.datasource import *

data_accessor = DataSource()

class TestDataSource(unittest.TestCase):

    def test_get_access_rows_by_demographic(self, demographic):

        expected = 
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), , "Should be: " + str(expected))

    def test_get_access_rows_by_demographic_EDGECASE(self, demographic):

        expected = 
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), , "Should be: " + str(expected))

    def test_get_use_rows_by_demographic(self, demographic):

        expected = 
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), , "Should be: " + str(expected))

    def test_get_use_rows_by_demographic_EDGECASE(self, demographic):

        expected = 
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), , "Should be: " + str(expected))