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
        result=arr.sort()
        self.assertEqual(result,quickSort(arr,True))
    def test_3(self):
        arr=[random.randrange(100)for x in range(10000)]
        result=arr.sort()
        self.assertEqual(result,quickSort(arr,True))
    def test_4(self):
        arr=[random.randrange(100)for x in range(10000)]
        result=arr.sort()
        self.assertEqual(result,quickSort(arr))
    def test_5(self):
        arr=[]
        arr2=arr
        result1=quickSort(arr)
        result2=quickSort(arr2,True)
        self.assertEqual(result1,result2)

    def test_6(self):
        arr=[random.randrange(100) for x in range(30)]
        arr2=arr
        result1=quickSort(arr)
        result2=quickSort(arr2,True)
        self.assertEqual(result1,result2)

if __name__=='__main__':
    unittest.main()