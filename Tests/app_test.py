from xarray import load_dataset
from app import *
import unittest

class TestFlaskApp(unittest.TestCase):
 
    """This is the test for the information on the homepage"""
    def test_route_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"This is the homepage for Team D's Project Component #2.\
    To see how often people of a certain demographic use birth control\
    when they are not trying to get pregnant, add /birth-control-use/[DEMOGRAPHIC] to the current url.\
    To see how concerned people of a certain demographic are about future access to birth control\
    due to the political climate, add /birth-control-access/[DEMOGRAPHIC] to the current url.\
            Here are some d `emographic ideas to input:<br><pre><font face=\"Times New Roman\">\
            * state abbreviation (ex. MN, MA, HI)<br>\
            * religion (ex. Hindu, Protestant, Jewish/Judaism, etc)<br>\
            * education level<br>\
                - Two year associate degree from a college or university<br>\
                - High school graduate (Grade 12 with diploma or GED certificate)<br></pre></font>",response.data)
 
    
    
    """This is the base case test for the correctness of information shown on the page when users want to search for birth control access by Hindu"""
    def test_route_access(self):
        self.app=app.test_client()
        display=self.app.get('/birth-control-access/Hindu',follow_redirects=True)
        self.assertEqual(b"{\"Don't know\":0,\"Not applicable/don't believe in birth control\":0,\"Not at all concerned\":20,\"Not very concerned\":0,\"Refused\":0,\"Somewhat concerned\":40,\"Very concerned\":40}\n",display.data)




    """This is the base case test for the correctness of information shown on the page when users want to search for birth control uses by Protestant"""
    def test_route_uses(self):
        self.app=app.test_client()
        display=self.app.get('/birth-control-use/Protestant',follow_redirects=True)
        self.assertEqual(b"{\"About half the time\":2,\"Almost every time\":4,\"Every time\":22,\"Never\":49,\"Not applicable/Does not have vaginal intercourse/sex\":18,\"Once in a while\":4}\n",display.data)


 
    
    """This is the edge case test when users give a name that is not in out dataset when searching for birth_control_access"""
    def test_route_access_edge(self):
        self.app=app.test_client()
        response=self.app.get('/birth-control-access/invalid',follow_redirects=True)
        self.assertEqual(b'Invalid Input. The demographic you chose is not in our dataset. Plase try another one.',response.data)

    """This is the edge case test to test when users give a name that is not in out dataset when searching for birth_control_uses"""
    def test_route_uses_edge(self):
        self.app=app.test_client()
        response=self.app.get('/birth-control-access/random',follow_redirects=True)
        self.assertEqual(b'Invalid Input. The demographic you chose is not in our dataset. Plase try another one.',response.data)

    """This is the base case test to test when users did not find the correct route name"""
    def test_not_found_error(self):
        self.app=app.test_client()
        response = self.app.get('/error_route') 
        self.assertEqual(b"Oops! You've encountered an error. Double check your spelling and \
        make sure to follow the format from the homepage\
        by adding either /birth-control-use/[DEMOGRAPHIC] or /birth-control-access/[DEMOGRAPHIC] \
            to the url! Head back to the homepage if you need demographic ideas. \
                If you follow these directions and\
            encounter an empty list, your demographic is not included in the dataset.",response.data) 

if __name__ == '__main__':
   
    unittest.main()