import unittest
from eval import eval_tree, eval_array_2

class treeEvaluator(unittest.TestCase):
    def test1(self):
        tree=['/',['*',['+',[9],[2]],['-',[6],[4]]],['*',['+',[10],[12]],[4]]]
        env=[['a',8],['b',2]]
        res=eval_tree(tree,env)
        self.assertEqual(res,0.25)
    def test2(self):
        tree = ['*',['/',[4],[2]],['+',[8],[4]]]
        env =[['a',4],['b',2],['c',8],['d',4]]
        res=eval_tree(tree,env)
        self.assertEqual(res,24)
    def test3(self):
        tree = ['*',['*',['/',['b'],['a']],['+',[8],[4]]],['*',['/',['c'],[2]],['+',[8],[4]]]]
        env=[['a',4],['b',2]]
        res=eval_tree(tree,env)
        self.assertEqual(res,None)
    def test4(self):
        tree=["+", ["a", [], []], ["*", ["b", [], []], ["/", ['c'], [1]]]]
        env=[['a',15],['b',5],['c',2]]
        res=eval_tree(tree,env)
        self.assertEqual(res,25)
    def test5(self):
        tree=["+", ["a", [], []], ["*", ["b", [], []], ["+", [610], ["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]]]]]
        env=[["a", 10], ["b", 20], ["c", 30]]
        res=eval_tree(tree,env)
        self.assertEqual(res,24410)
if __name__=='__main__':
    unittest.main()