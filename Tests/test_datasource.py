import unittest

from ProductionCode.datasource import *

data_accessor = DataSource()

class TestDataSource(unittest.TestCase):

    def test_get_access_rows_by_demographic(self, demographic):

        expected = [('Very concerned',), ('Not at all concerned',), ('Somewhat concerned',), ('Somewhat concerned',), ('Very concerned',)]
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_get_access_rows_by_demographic_EDGECASE(self, demographic):

        expected = []
        self.assertEqual(data_accessor.get_access_rows_by_demographic("hindu"), [], "Should be: " + str(expected))

    def test_get_use_rows_by_demographic(self, demographic):

        expected = [('Every time',), ('Never',), ('Every time',), ('Not applicable/Does not have vaginal intercourse/sex',), ('Never',)]
        self.assertEqual(data_accessor.get_access_rows_by_demographic("Hindu"), [('Every time',), ('Never',), ('Every time',), ('Not applicable/Does not have vaginal intercourse/sex',), ('Never',)], "Should be: " + str(expected))

    def test_get_use_rows_by_demographic_EDGECASE(self, demographic):

        expected = []
        self.assertEqual(data_accessor.get_access_rows_by_demographic("hindu"), [], "Should be: " + str(expected))