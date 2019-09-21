import unittest

from MySolution import Stack
from MySolution import infixToPostfix
from MySolution import evaluate_postfix

class convert_tester(unittest.TestCase):

    def convert_emptyString(self):
        result = infixToPostfix('')
        self.assertEqual(result,'')

    def convert_noOperands(self):
        result = infixToPostfix('+*/')
        self.assertEqual('+*/')

    def convert_noOperators(self):
        result = infixToPostfix('12341231')
        self.assertEqual('12341231')

class evaluate_tester(unittest.TestCase):

    def evaluate_noOperators(self):
        result = evaluate_posftix('1234')
        self.assertEqual(result,'1234')

    def evaluate_noOperands(self):
        result = evaluate_postifx('+/*')
        self.assertEqual(result,'+/*')
if __name__=='__main__':
    unittest.main()
