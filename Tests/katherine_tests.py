import unittest
from birth_control import *

class TestBirthControl(unittest.TestCase):
    def setUp(self):
        load_data()
    def test_display_list(self):
        """Asserts that the list passed into the function
        is indeed displayed, and that the displayed list is correct"""
        myList = ["Katherine", "Ella", "Evelyn"]
        self.assertEqual(display_list(myList), myList, "Should be " + myList)
    #def test_load_data(self):
        #"""Asserts the data is loaded correctly"""
        #What are we asserting equal to each other? or, do we use a different type of test?
    #def test_look_up_use_of_birth_control_by_religion(self):
        #"""Asserts that the use of birth control by religion is being looked up"""
        #This one is stupid...what do I do
    def test_get_user_ids_by_column_for_religion(self):
        """Affirms that the user ids for the correct religion are returned"""
        ids = [50000198, 50000290,  70000589, 70000664, 70000805]
        self.assertEqual(get_user_ids_by_column_for_religion("Hindu"), ids, "Should be " + print(ids))
    def test_get_use_of_birth_control(self):
        """Affirms the correct list of birth control usage is displayed"""
        ids = [50000198, 50000290,  70000589, 70000664, 70000805]
        output = ['Every time', 'Never', 'Every time', 'Not applicable/Does not have vaginal intercourse/sex', 'Never']
        self.assertEqual(get_use_of_birth_control(ids), output, "Should be " + print(output))

if __name__ == '__main__':
    unittest.main()