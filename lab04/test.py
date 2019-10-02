import unittest
from mySolution import power,powerH,C

class mathTester(unittest.TestCase):
    def test_power(self):
        result = power(8,6,1)
        self.assertEqual(result,262144)
    def test_power2(self):
        result = power(6,9,1)
        self.assertEqual(result,10077696)
    
    def test_powerH(self):
        result = powerH(8,6)
        self.assertEqual(result,262144)
    def test_powerH2(self):
        result = powerH(6,9)
        self.assertEqual(result,10077696)
    def test_C(self):
        result = C(13,6)
        self.assertEqual(result,1716)
if __name__=='__main__':
    unittest.main()
