import unittest

from ProductionCode.datasource import *

data_accessor = DataSource()

class TestDataSource(unittest.TestCase):

    def test_get_access_column_by_demographic(self):
        """
        Ensures that valid input returns the correct list of responses.
        """

        expected = [('Very concerned',), ('Not at all concerned',), ('Somewhat concerned',), ('Somewhat concerned',), ('Very concerned',)]
        self.assertEqual(data_accessor.get_access_column_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_get_access_column_by_demographic_EDGECASE(self):
        """
        Ensures that when the function is passed an invalid argument (i.e. hindu)
        that is misspelled or not capitalized correctly, an empty list is returned.
        """

        expected = []
        self.assertEqual(data_accessor.get_access_column_by_demographic("hindu"), [], "Should be: " + str(expected))

    def test_get_use_column_by_demographic(self):
        """
        Ensures that when valid input is passed, the correct responses are returned.
        """

        expected = [('Every time',), ('Never',), ('Every time',), ('Not applicable/Does not have vaginal intercourse/sex',), ('Never',)]
        self.assertEqual(data_accessor.get_use_column_by_demographic("Hindu"), [('Every time',), ('Never',), ('Every time',), ('Not applicable/Does not have vaginal intercourse/sex',), ('Never',)], "Should be: " + str(expected))

    def test_get_use_column_by_demographic_EDGECASE(self):
        """
        Ensured that when an invalid argument is passed that is not spelled
        or capitalized correctly, an empty list is returned.
        """

        expected = []
        self.assertEqual(data_accessor.get_use_column_by_demographic("hindu"), [], "Should be: " + str(expected))