import unittest
import subprocess
from ProductionCode.birth_control import *


class TestBirthControl(unittest.TestCase):

    def setUp(self):
        load_data()

    def test_load_data(self):
        """
        Ensures the load data function does not return any errors.
        """
        self.assertIsNone(load_data())

    def test_display_results(self):
        """
        Asserts that the list passed into the display_list function
        is indeed displayed, and that the displayed list is correct for the input provided.
        """
        exampleDictToDisplay = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":40,
            "Never":40,
            "Not applicable/Does not have vaginal intercourse/sex":20,
            "Once in a while":0
        }
        self.assertEqual(display_results(exampleDictToDisplay), exampleDictToDisplay, "Should be " + str(exampleDictToDisplay))

    def test_look_up_birth_control_access_by_demographic(self):
        """
        Asserts that the responses to the question about concerns regarding future
        birth control access are being accuratlely looked up and returned.
        """
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":20,
            "Not very concerned":0,
            "Refused":0,
            "Somewhat concerned":40,
            "Very concerned":40
        }
        self.assertEqual(look_up_birth_control_access_concerns_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_look_up_birth_control_access_by_demographic_EDGECASE(self):
        """
        Asserts that when invalid input is provided, the function
        returns the dictionary with no percentage values to indicate
        that the demographic is not included in the dataset.
        """
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":0,
            "Not very concerned":0,
            "Refused":0,
            "Somewhat concerned":0,
            "Very concerned":0
        }
        self.assertEqual(look_up_birth_control_access_concerns_by_demographic("vegetarian"), expected, "Should be: " + str(expected))

    def test_look_up_use_of_birth_control_by_demographic(self):
        """
        Asserts that the use of birth control by demographic is being looked up
        and returning the correct dictionary.
        """
        expected = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":40,
            "Never":40,
            "Not applicable/Does not have vaginal intercourse/sex":20,
            "Once in a while":0
        }
        self.assertEqual(look_up_use_of_birth_control_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_look_up_use_of_birth_control_by_demographic_EDGECASE(self):
        """
        Tests the edge case of the function receiving input
        that is not valid, i.e. misspelled or not in database.
        """
        invalidReligion = "Flying Spaghetti Monster"
        expected = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":0,
            "Never":0,
            "Not applicable/Does not have vaginal intercourse/sex":0,
            "Once in a while":0
        }
        self.assertEqual(look_up_use_of_birth_control_by_demographic(invalidReligion), expected, "Should be: " + str(expected))

    def test_get_user_ids_by_column(self):
        """
        Affirms that the user ids for the correct demographic are returned
        """
        ids = ['50000198', '50000290', '70000589', '70000664', '70000805']
        self.assertEqual(get_user_ids_by_column("Hindu"), ids, "Should be " + str(ids))

    def test_get_user_ids_by_column_EDGECASE(self):
        """
        Affirms no user ids are returned if the demogrpahic input is invalid
        and that the error message is printed.
        """
        invalidReligion = "Flying Spaghetti Monster"
        self.assertEqual(get_user_ids_by_column(invalidReligion), [], "Should be: " + str([]))

    def test_get_use_of_birth_control(self):
        """
        Affirms the correct list of birth control usage is displayed based on the demographic.
        """
        ids = ['50000198', '50000290',  '70000589', '70000664', '70000805']
        output = ['Every time', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never']
        self.assertEqual(get_use_of_birth_control(ids), output, "Should be " + str(output))

    def test_get_use_of_birth_control_EDGECASE(self):
        """
        Affirms that a message is printed if the function
        is passed an empty list as input.
        """
        self.assertEqual(get_use_of_birth_control([]), [], "Should be: " + str([]))

    def test_get_birth_control_access_concerns(self):
        """
        Affirms that the correct list of responses
        is returned according to the demographic input.
        """
        ids = ['50000198', '50000290',  '70000589', '70000664', '70000805']
        expected = ["Very concerned",
            "Not at all concerned",
            "Somewhat concerned",
            "Somewhat concerned",
            "Very concerned"
            ]
        self.assertEqual(get_birth_control_access_concerns(ids), expected, "Should be: " + str(expected))

    def test_get_birth_control_access_concerns_EDGECASE(self):
        """
        Affirms that if invalid input or an empty list is passed in,
        an empty list is returned to signal that there was an issue.
        """
        self.assertEqual(get_birth_control_access_concerns([]), [], "Should be: " + str([]))
        
    def test_count_birth_control_use_answers(self):
        """
        Affirms that the function outputs the correct
        dictionary and counts for the list it is passed in.
        """

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