import unittest
from hashing import hashtable
import random

class hash_test(unittest.TestCase):
    def test_1(self): #This test is for the functionality of the map resizing
        keys=[9,15,28,93]
        data=[11,12,13,14]
        t=hashtable(5) 
        for i in range(len(keys)):
            t.put(keys[i],data[i])
        res=t.get_data()
        self.assertEqual(res,[12,14,None,13,11]) #after putting our items in the table the load factor is 80%
        t.put(55,15) #when we put in another value, the load factor is calculated and determined to be in excess of 75% and therfore resizes the map
        res=t.get_data()
        self.assertEqual(res,[None, None, None, 14, None, 12, 15, None, 13, 11]) #if the resize is carried out correctly, the map is doubled and all values are rehashed and mapped accordingly

    def test_2(self): #This test is for the functionality of the map resizing
        keys=[54,21,75]
        data=[1,2,3]
        t=hashtable(4)
        for i in range(len(keys)):
            t.put(keys[i],data[i])
        res = t.get_data()
        self.assertEqual(res,[None, 2, 1, 3])#loadfactor is 75%
        t.put(89,4)#our threshold is not exceeded, therefore put can go forward 
        res=t.get_data()
        self.assertEqual(res,[4, 2, 1, 3])#loadfactor is 100%
        t.put(64,5)#our threshold is exceeded, therefore prior to putting we resize the map, and rehash and put all values
        res=t.get_data()
        self.assertEqual(res,[5, 4, None, 3, None, 2, 1, None])

    def test_put(self):
        t=hashtable(6)
        res=t.get_data()
        self.assertEqual(res,[None,None,None,None,None,None])
        t.put(59,3)
        self.assertEqual(res,[None,None,None,None,None,3])
    
    def test_collision(self):#our hash function uses key%size to find the position, therefore 55%5=60%5. When it tries to put '2' in the map it will collide, and move forward to next available position
        t=hashtable(5)
        t.put(55,1)
        t.put(60,2)
        res=t.get_data()
        self.assertEqual(res,[1,2,None,None,None])
    
    def test_update(self):
        t=hashtable(5)
        t.put(55,1)
        t.put(55,3)
        res=t.get_data()
        self.assertEqual(res,[3,None,None,None,None])

    def test_get(self):
        t=hashtable(5)
        keys=[9,15,28,93]
        data=[11,12,13,14]
        t=hashtable(5) 
        for i in range(len(keys)):
            t.put(keys[i],data[i])
        res=t.get_data()
        self.assertEqual(res,[12,14,None,13,11])
        t.put(55,15)
        res=t.get_data()
        self.assertEqual(res,[None, None, None, 14, None, 12, 15, None, 13, 11])
        res=t.get(55)
        self.assertEqual(res,15)

if __name__=='__main__':
    unittest.main()