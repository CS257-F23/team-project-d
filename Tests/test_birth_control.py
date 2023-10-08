import unittest
import subprocess
from ProductionCode.birth_control import *

# clean these up with the new production code

class TestBirthControl(unittest.TestCase):

    def setUp(self):
        load_data()

    def test_load_data(self):
        """ensures load data function does not return any errors"""
        self.assertIsNone(load_data())

    def test_display_results(self):
        """Asserts that the list passed into the display_list function
        is indeed displayed, and that the displayed list is correct for the input provided"""
        myList = ["Katherine", "Ella", "Evelyn"]
        self.assertEqual(display_results(myList), myList, "Should be " + str(myList))

    def test_look_up_use_of_birth_control_by_religion(self):
        """Asserts that the use of birth control by religion is being looked up
        and not returning any errors"""
        message = "Test value is not none."
        self.assertIsNone(look_up_use_of_birth_control_by_demographic("Hindu"), message)

    def test_look_up_use_of_birth_control_by_religion_EDGECASE(self):
        """Tests the edge case of the function receiving input
        that is not valid, i.e. misspelled or not in database"""
        invalidReligion = "Flying Spaghetti Monster"
        self.assertRaises(IndexError, look_up_use_of_birth_control_by_demographic, invalidReligion)

    def test_get_user_ids_by_column_for_religion(self):
        """Affirms that the user ids for the correct religion are returned"""
        ids = ['50000198', '50000290', '70000589', '70000664', '70000805']
        self.assertEqual(get_user_ids_by_column("Hindu"), ids, "Should be " + str(ids))

    def test_get_user_ids_by_column_for_religion_EDGECASE(self):
        """Affirms no user ids are returned if religion input is invalid
        and that IndexError is thrown"""
        invalidReligion = "Flying Spaghetti Monster"
        self.assertRaises(IndexError, get_user_ids_by_column, invalidReligion)

    def test_get_use_of_birth_control(self):
        """Affirms the correct list of birth control usage is displayed"""
        ids = ['50000198', '50000290',  '70000589', '70000664', '70000805']
        output = ['Every time', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never']
        self.assertEqual(get_use_of_birth_control(ids), output, "Should be " + str(output))

    def test_get_use_of_birth_control_EDGECASE(self):
        """Affirms that an error is raised if the function
        is passed an empty list as input"""
        self.assertRaises(IndexError, get_use_of_birth_control, [])

    def test_look_up_use_of_birth_control_by_education_level(self):
        """ensure no errors are returned"""
        self.assertIsNone(look_up_use_of_birth_control_by_demographic("Less than high school (Grades 1-8 or no formal schooling)"))

    def test_edge_look_up_use_of_birth_control_by_education_level(self):
        """edge case for if topic entered into lookup function is not included in the dataset"""
        self.assertRaises(IndexError, look_up_use_of_birth_control_by_demographic, "Nonexistent education level")

    def test_get_user_ids_by_column_for_educ(self):
        """example test for education level"""
        ids= ['50000211','50000290','50000354','50000355','50000385','50000390','70000080','70000113','70000136','70000155','70000292',
        '70000315','70000325','70000350','70000498','70000515','70000548','70000590','70000682','70000762','70000794','70000859']
        #load_data()
        outcome= get_user_ids_by_column("Less than high school (Grades 1-8 or no formal schooling)")
        self.assertEqual(outcome, ids, "Should be " + str(ids))
    
    def test_edge_get_user_ids_by_column_for_educ(self):
        """tests edge case that if education level is not included in the dataset returns error for function called by lookup function"""
        self.assertRaises(IndexError, get_user_ids_by_column, "Nonexistent education level")

    def test_main(self):
        """check if birth_control.py works for valid command line argument"""
        code=subprocess.Popen(['python3','birth_control.py','--religion','Protestant'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        expected=['Never', 'Every time', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Every time', 'Never', 'Every time', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Every time', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Never', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Every time', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Never', 'Never', 'Never', 'Almost every time', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Once in a while', 'Once in a while', 'Never', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Every time', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Every time', 'Never', 'Every time', 'Never', 'Never', 'Once in a while', 'Every time', 'Every time', 'Never', 'Every time', 'Almost every time', 'Never', 'Never', 'Every time', "Don't know", 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Every time', 'Never', 'Refused', 'Every time', 'Never', 'Never', 'Every time', 'Refused', 'Every time', 'Refused', 'Never', 'Never', 'Never', 'Never', 'Never', 'Never', 'Never', 'Once in a while', 'Never', 'Every time', 'Never', 'Every time', 'Every time', 'Never', 'Every time', 'Every time', 'Every time', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Refused', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'Every time', 'Every time', 'Never', 'Never', 'Never', 'Never', 'Never', 'Never', 'Not applicable/Does not have vaginal intercourse/sex', 'About half the time', 'Every time', 'Never', 'Never', 'Every time', 'Never', 'About half the time', 'Never', 'Never', 'Never', 'Almost every time', 'Never', 'Never', 'Every time', 'Every time', 'Never', 'Never', 'Almost every time', 'Every time', 'Never', 'Every time', 'Never', 'Never', 'About half the time', 'Never', 'Never', 'Almost every time', 'Once in a while', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Every time', 'Every time', 'Every time', 'Never', 'Almost every time', 'Almost every time', 'Never', 'Once in a while', 'Every time', 'Every time', 'Once in a while', 'Never', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'About half the time', 'Not applicable/Does not have vaginal intercourse/sex', 'Almost every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Almost every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never', 'Once in a while', 'Every time', 'Every time', 'Every time', 'Every time']  
        # Now, you can compare the actual_output_list with the expected output
        self.assertEqual(output.strip(),str(expected))
        code.terminate()

    def test_main_edge(self):
        """This is an edge case test. Check if birth_control.py works for invalid command line argument"""
        code=subprocess.Popen(['python3','birth_control.py','--state'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        self.assertIn(output.strip(),"Usage: python3 birth_control.py --educ or --religion")
        code.terminate()

if __name__ == '__main__':
    unittest.main()