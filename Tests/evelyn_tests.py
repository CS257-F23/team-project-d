# -*- coding: utf-8 -*-

import unittest
import subprocess

from ProductionCode.birth_control import *

# Rest of your code...



class TestMethods(unittest.TestCase):
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

    
    
load_data()
if __name__ == '__main__':
    unittest.main()