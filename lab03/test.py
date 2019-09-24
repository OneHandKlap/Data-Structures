import unittest

from MySolution import Stack
from MySolution import infixToPostfix
from MySolution import evaluate_postfix
from MySolution import factorial

class evaluate_tester(unittest.TestCase):


    def test_evaluate(self):
        result = evaluate_postfix(infixToPostfix('(1+4)*(5+6)-(6/3)*3!'))
        self.assertEqual(result,43)

    def test_evaluate2(self):
        result = evaluate_postfix(infixToPostfix('4!+8*(2/5)-4+(9/3)'))
        print(infixToPostfix('4!+8*(2/5)-4+(9/3)'))
        self.assertEqual(result,26.2)

    def test_evaluate3(self):
        result = evaluate_postfix('1+2/(4*3)')
        print(result)
        self.assertEqual(result,'2.5')

    def test_evaluate4(self):
        result = evaluate_postfix('(9+1)/2*8+(5-2)')
        print(result)
        self.assertEqual(result,'43')
        

if __name__=='__main__':
    unittest.main()
