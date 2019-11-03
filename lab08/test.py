import unittest
from parser import precedence, operatorp, numberp , parse, parseHelper, handleOp

class parseTester(unittest.TestCase):
    def test1(self):
        item=[['4', '+', '3'], '*', '7']
        res=parse(item)
        self.assertEqual(res, 	['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])

    def test2(self):
        item=['4', '+', [['3', '+', '1'], '!']]
        res=parse(item)
        self.assertEqual(res,['+', ['4', [], []], ['!', ['+', ['3', [], []], ['1', [], []]], []]])

    def test3(self):
        item=['3','/',['6', '!'],'-', '9']
        res=parse(item)
        self.assertEqual(res, 	['-', ['/', ['3', [], []], ['!', ['6', [], []], []]], ['9', [], []]])

if __name__=="__main__":
    unittest.main()