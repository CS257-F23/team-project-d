import unittest
import subprocess
from ProductionCode.birth_control import *
from cl import *
data_accessor = BirthControl()


class TestBirthControl(unittest.TestCase):

    def setUp(self):
        data_accessor.load_data()

    def test_load_data(self):
        """
        Ensures the load data function does not return any errors.
        """
        self.assertIsNone(data_accessor.load_data())

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
        self.assertEqual(data_accessor.display_results(exampleDictToDisplay), exampleDictToDisplay, "Should be " + str(exampleDictToDisplay))

    def test_get_birth_control_access_by_demographic(self):
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
        self.assertEqual(data_accessor.get_birth_control_access_concerns_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_get_birth_control_access_by_demographic_EDGECASE(self):
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
        self.assertEqual(data_accessor.get_birth_control_access_concerns_by_demographic("vegetarian"), expected, "Should be: " + str(expected))

    def test_get_use_of_birth_control_by_demographic(self):
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
        self.assertEqual(data_accessor.get_use_of_birth_control_by_demographic("Hindu"), expected, "Should be: " + str(expected))

    def test_get_use_of_birth_control_by_demographic_EDGECASE(self):
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
        self.assertEqual(data_accessor.get_use_of_birth_control_by_demographic(invalidReligion), expected, "Should be: " + str(expected))
        
    def test_count_birth_control_use_answers(self):
        """
        Affirms that the function outputs the correct
        dictionary and counts for the list it is passed in.
        """
        testListOfResponses = [('Never',), ('Every time',)]
        expected = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":1,
            "Never":1,
            "Not applicable/Does not have vaginal intercourse/sex":0,
            "Once in a while":0
        }
        self.assertEqual(data_accessor.count_birth_control_use_answers(testListOfResponses), expected, "Should be " + str(expected))

    def test_count_birth_control_use_answers_EDGECASE(self):
        """
        Affirms that if an empty list is input,
        the correct dictionary with no responses will be output.
        """
        expected = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":0,
            "Never":0,
            "Not applicable/Does not have vaginal intercourse/sex":0,
            "Once in a while":0
        }
        self.assertEqual(data_accessor.count_birth_control_use_answers([]), expected, "Should be: " + str(expected))

    def test_count_birth_control_access_answers(self):
        """
        Affirms that the function outputs the correct dictionary
        and numbers of responses for the list it is passed.
        """
        testListOfAccessAnswers = [('Refused',), ('Very concerned',), ('Not at all concerned',)]
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":1,
            "Not very concerned":0,
            "Refused":1,
            "Somewhat concerned":0,
            "Very concerned":1
        }
        self.assertEqual(data_accessor.count_birth_control_access_answers(testListOfAccessAnswers), expected, "Should be: " + str(expected))

    def test_count_birth_control_access_answers_EDGECASE(self):
        """
        Affirms that if the function is passed an empty list,
        A dictionary with all responses set to zero is returned.
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
        self.assertEqual(data_accessor.count_birth_control_access_answers([]), expected, "Should be: " + str(expected))

    def test_calc_percentage(self):
        """
        Affirms the calc_percentage function accurately
        calculates the percentages based on the list of 
        responses it is given, and returns them in the
        correct format. 
        """
        totaled_answers = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":0,
            "Not very concerned":4,
            "Refused":0,
            "Somewhat concerned":0,
            "Very concerned":4
        }
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":0,
            "Not very concerned":50,
            "Refused":0,
            "Somewhat concerned":0,
            "Very concerned":50
        }
        self.assertEqual(data_accessor.calc_percentage(totaled_answers), expected, "Should be: " + str(expected))

    def test_calc_percentage_EDGECASE(self):
        """
        Affirms the calc_percentage function will output
        an empty dictionary if it is passed an empty dictionary. 
        """
        self.assertEqual(data_accessor.calc_percentage({}), {}, "Should be: " + str({}))


    def test_count_birth_control_use_answers_EDGECASE(self):
        """
        Affirms that if an empty list is input,
        the correct dictionary with no responses will be output.
        """
        expected = {
            "About half the time":0,
            "Almost every time":0,
            "Every time":0,
            "Never":0,
            "Not applicable/Does not have vaginal intercourse/sex":0,
            "Once in a while":0
        }
        self.assertEqual(data_accessor.count_birth_control_use_answers([]), expected, "Should be: " + str(expected))

    def test_count_birth_control_access_answers(self):
        """
        Affirms that the function outputs the correct dictionary
        and numbers of responses for the list it is passed.
        """
        testListOfAccessAnswers = [('Refused',), ('Very concerned',), ('Not at all concerned',)]
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":1,
            "Not very concerned":0,
            "Refused":1,
            "Somewhat concerned":0,
            "Very concerned":1
        }
        self.assertEqual(data_accessor.count_birth_control_access_answers(testListOfAccessAnswers), expected, "Should be: " + str(expected))

    def test_count_birth_control_access_answers_EDGECASE(self):
        """
        Affirms that if the function is passed an empty list,
        A dictionary with all responses set to zero is returned.
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
        self.assertEqual(data_accessor.count_birth_control_access_answers([]), expected, "Should be: " + str(expected))

    def test_calc_percentage(self):
        """
        Affirms the calc_percentage function accurately
        calculates the percentages based on the list of 
        responses it is given, and returns them in the
        correct format. 
        """
        totaled_answers = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":0,
            "Not very concerned":4,
            "Refused":0,
            "Somewhat concerned":0,
            "Very concerned":4
        }
        expected = {
            "Don't know":0,
            "Not applicable/don't believe in birth control":0,
            "Not at all concerned":0,
            "Not very concerned":50,
            "Refused":0,
            "Somewhat concerned":0,
            "Very concerned":50
        }
        self.assertEqual(data_accessor.calc_percentage(totaled_answers), expected, "Should be: " + str(expected))

    def test_calc_percentage_EDGECASE(self):
        """
        Affirms the calc_percentage function will output
        an empty dictionary if it is passed an empty dictionary. 
        """
        self.assertEqual(data_accessor.calc_percentage({}), {}, "Should be: " + str({}))



    def test_main_BirthControlUseByDemo(self):
        """
        Affirms that birth_control.py works for valid command line argument --BirthControlUseByDemo
        and returns the correct output and format.
        """
        code=subprocess.Popen(['python3','ProductionCode/birth_control.py','--BirthControlUseByDemo','Protestant'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        expected= """How often do you use birth control? Demographic: Protestant
Never : 49 %
Not applicable/Does not have vaginal intercourse/sex : 18 %
Every time : 22 %
About half the time : 2 %
Once in a while : 4 %
Almost every time : 4 %"""
        self.assertIn(output.strip(),str(expected))
        code.terminate()

    def test_main_BirthControlAccessByDemo(self):
        """
        Affirms that birth_control.py works for valid command line argument --BirthControlAccessByDemo
        and returns the correct output and format. 
        """
        code=subprocess.Popen(['python3','cl.py','--BirthControlAccessByDemo','Hindu'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        expected="""Given the current political climate (2020), how concerned are you with birth control access in the future? Demographic: Hindu
Very concerned : 40 %
Not applicable/don't believe in birth control : 0 %
Somewhat concerned : 40 %
Not very concerned : 0 %
Not at all concerned : 20 %
Don't know : 0 %
Refused : 0 %"""
        self.assertIn(output.strip(),str(expected))
        code.terminate()

    def test_main_options(self):
        """
        Affirms that birth_control.py works for valid command line argument --option
        and outputs the options available to input in the correct format. 
        """
        code=subprocess.Popen(['python3','cl.py','--option'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        self.assertEqual(output.strip(),optionsDisplay())
        code.terminate()

    def test_empty_args(self):
        """
        This is an edge case test. Check if birth_control.py prints the usage for no command line argument.
        """
        code=subprocess.Popen(['python3', 'cl.py'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        self.assertEqual(output.strip(),Usage())
        code.terminate()
    
    def test_Invalid_args(self):
        """
        This is an edge case test. Check if birth_control.py prints the usage for invalid command line arguments.
        """
        code=subprocess.Popen(['python3', 'cl.py','--invalid'],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              encoding='utf8')
        output, err=code.communicate()
        self.assertIn(output.strip(),Usage())
        code.terminate()


if __name__ == '__main__':
    unittest.main()