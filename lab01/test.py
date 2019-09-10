import unittest
from mySolution import generate
from mySolution import calculate_score
from collections import OrderedDict

class generate_tester(unittest.TestCase):

    def test_long(self):
        result = generate(100000)
        self.assertEqual(len(result),100000)

    def test_short(self):
        result = generate(0)
        self.assertEqual(len(result),0)
        self.assertIs

    def test_random(self):
        result_1=generate(15)
        result_2=generate(15)
        self.assertNotEqual(result_1,result_2)

class calculate_tester(unittest.TestCase):

    def test_uneven(self):
        result = calculate_score('qwerty','qwe')
        desired_result={}
        desired_result[0]='q'
        desired_result[1]='w'
        desired_result[2]='e'
        self.assertEqual(result,desired_result)

    def test_goal_smaller(self):
        result = calculate_score('qwe','qwerty')
        desired_result={}
        desired_result[0]='q'
        desired_result[1]='w'
        desired_result[2]='e'   
        self.assertEqual(result,desired_result)
        
if __name__=='__main__':
    unittest.main()
