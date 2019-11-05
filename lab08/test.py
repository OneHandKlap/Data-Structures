import unittest
from parsing import precedence, operatorp, numberp , parse, parseHelper, handleOp

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

    def test4(self):
        item=[['4','+',['6','*','2']],'/','4']
        res=parse(item)
        self.assertEqual(res,['/',['+',['4',[],[]],['*',['6',[],[]],['2',[],[]]]],['4',[],[]]])

    def test5(self):
        item=[['5','+','2'],'*',['2','-','1']]
        res=parse(item)
        self.assertEqual(res,['*',['+',['5',[],[]],['2',[],[]]],['-',['2',[],[]],['1',[],[]]]])
    
if __name__=="__main__":
    unittest.main()