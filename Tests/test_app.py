from app import *
import unittest

data_accessor = BirthControl()

class TestFlaskApp(unittest.TestCase):
 
    def setUp(self):
        data_accessor.load_data()
    def createapp(self):
        return app

  

    """This is the base case test for the information on the homepage"""
    def test_route_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'About', response.data)

    """This is the base case test for the information on the search page for birth control uses"""
    def test_route_searchpage_use(self):
        self.app = app.test_client()
        response = self.app.get('/birth-control-use', follow_redirects=True)
        self.assertIn(b'Toggle through the options above to see demographic lookup options', response.data)
    

    """This is the base case test for the information on the search page for birth control accesses"""
    def test_route_searchpage_access(self):
        self.app = app.test_client()
        response = self.app.get('/birth-control-access', follow_redirects=True)
        self.assertIn(b'Toggle through the options above to see demographic lookup options', response.data)
    
    """This is the base case test for the correctness of information shown on the page when users want to search for birth control access by Hindu"""
    def test_route_access(self):
        self.app=app.test_client()
        display=self.app.get('/birth-control-access/Hindu',follow_redirects=True)
        expected="<p>Very concerned : 40 %</p>\n        \n        <p>Not applicable/don&#39;t believe in birth control : 0 %</p>\n        \n        <p>Somewhat concerned : 40 %</p>\n        \n        <p>Not very concerned : 0 %</p>\n        \n        <p>Not at all concerned : 20 %</p>\n        \n        <p>Don&#39;t know : 0 %</p>\n        \n        <p>Refused : 0 %</p>\n "
        expected_bytes = expected.encode('utf-8') 
        self.assertIn(expected_bytes,display.data)




    """This is the base case test for the correctness of information shown on the page when users want to search for birth control uses by Protestant"""
    def test_route_uses(self):
        self.app=app.test_client()
        display=self.app.get('/birth-control-use/Protestant',follow_redirects=True)
        expected= "<p>Never : 49 %</p>\n        \n        <p>Not applicable/Does not have vaginal intercourse/sex : 18 %</p>\n        \n        <p>Every time : 22 %</p>\n        \n        <p>About half the time : 2 %</p>\n        \n        <p>Once in a while : 4 %</p>\n        \n        <p>Almost every time : 4 %</p>\n  "
        expected_bytes = expected.encode('utf-8') 
        self.assertIn(expected_bytes,display.data)


 
    
    """This is the edge case test when users give a name that is not in out dataset when searching for birth_control_access"""
    def test_route_access_edge(self):
        self.app=app.test_client()
        response=self.app.get('/birth-control-access/invalid',follow_redirects=True)
        self.assertIn(b"Very concerned : 0 %",response.data) 

    """This is the edge case test to test when users give a name that is not in out dataset when searching for birth_control_uses"""
    def test_route_uses_edge(self):
        self.app=app.test_client()
        response=self.app.get('/birth-control-access/random',follow_redirects=True)
        self.assertIn(b"Very concerned : 0 %",response.data) 

    """This is the base case test to test when users did not find the correct route name"""
    def test_not_found_error(self):
        self.app=app.test_client()
        response = self.app.get('/error_route') 
        self.assertIn(b"The page you are looking for does not exist.",response.data) 

if __name__ == '__main__':
   
    unittest.main()