import unittest
from birth_control import *

class TestEducationFunctions(unittest.TestCase):
    def test_look_up_use_of_birth_control_by_education_level(self):
        """ensure no errors are returned"""
        self.assertIsNone(look_up_use_of_birth_control_by_education_level("Less than high school (Grades 1-8 or no formal schooling)"))

    def test_edge_look_up_use_of_birth_control_by_education_level(self):
        """edge case for if topic entered into lookup function is not included in the dataset"""
        self.assertRaises(IndexError, look_up_use_of_birth_control_by_education_level, "Nonexistent education level")

    def test_get_user_ids_by_column_for_educ(self):
        """example test for education level"""
        ids= ['50000211','50000290','50000354','50000355','50000385','50000390','70000080','70000113','70000136','70000155','70000292',
        '70000315','70000325','70000350','70000498','70000515','70000548','70000590','70000682','70000762','70000794','70000859']
        load_data()
        outcome= get_user_ids_by_column_for_educ("Less than high school (Grades 1-8 or no formal schooling)")
        self.assertEqual(outcome, ids, "Should be 50000211,50000290,50000354,50000355,50000385,50000390,70000080,70000113,70000136,70000155,70000292,70000315,70000325,70000350,70000498,70000515,70000548,70000590,70000682,70000762,70000794,70000859")
    def test_edge_get_user_ids_by_column_for_educ(self):
        """tests edge case that if education level is not included in the dataset returns error for function called by lookup function"""
        self.assertRaises(IndexError, get_user_ids_by_column_for_educ, "Nonexistent education level")
    def test_load_data(self):
        """ensures load data function does not return any errors"""
        self.assertIsNone(load_data())
