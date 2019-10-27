import unittest
import random
from sorting import quickSort,quickSortHelper,partition

class quickSortTester(unittest.TestCase):
    def test_1(self):
        arr=[random.randrange(100) for x in range(10)]
        result = arr.sort()
        self.assertEqual(result,quickSort(arr))
    def test_2(self):
        arr=[random.randrange(1000) for x in range(100)]
        result=quickSort(arr)
        self.assertEqual(result,quickSort(arr,True))

if __name__=='__main__':
    unittest.main()