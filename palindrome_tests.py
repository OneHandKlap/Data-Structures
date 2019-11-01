import unittest
from Recursion_practice import ispalindrome, palin

class palindrometester(unittest.TestCase):
    def test1(self):
        s="tacocat"
        k=0
        res=palin(s,k)
        self.assertEqual(res,True)
    def test2(self):
        s="tacoca22t"
        k=2
        res=palin(s,k)
        self.assertEqual(res,True)
    def test3(self):
        s="asdasd"
        k=5
        res=palin(s,k)
        self.assertEqual(res,True)
    def test4(self):
        s="ssadd"
        k=4
        res=palin(s,k)
        self.assertEqual(res,True)
    def test5(self):
        s="alskkdajk"
        k=7
        res=palin(s,k)
        self.assertEqual(res,True)

if __name__ == "__main__":
    unittest.main()
