import unittest

from MySolution import Stack
from MySolution import infixToPostfix
from MySolution import evaluate_postfix

class convert_tester(unittest.TestCase):

    def convert_emptyString(self):
        result = infixToPostfix('')
        self.assertEqual(result,'Invalid string')

    def convert_noOperands(self):
        result = infixToPostfix('+*/')
        self.assertEqual(result,'Invalid string')

    def convert_noOperators(self):
        result = infixToPostfix('12341231')
        self.assertEqual(result,'Invalid string')

class evaluate_tester(unittest.TestCase):

    def evaluate_noOperators(self):
        result = evaluate_posftix('1234')
        self.assertEqual(result,'1234')

    def evaluate_noOperands(self):
        result = evaluate_postifx('+/*')
        self.assertEqual(result,'Invalid string')
if __name__=='__main__':
    unittest.main()
