class BinaryHeap():
    def __init__(self):
        self.data=[0]
        self.size=0
    def reHeapUp(self,i):
        while i//2>0: #while there are items in our heap
            if self.data[i]<self.data[i//2]: #if this item is smaller than its parent, swap this item and its parent
                temp =self.data[i//2]
                self.data[i//2]=self.data[i]
                self.data[i]=temp
            i=i//2 #move up a level in the tree
    def insert(self,array):
        for i in array:
            self.data.append(i)
            self.size+=1
            self.reHeapUp(self.size)
    def getRoot(self):
        return self.data[1]
    def reHeapDown(self,i): #this will almost always be called when i=1 or for the item at the top of the heap
        while(i*2)<=self.size: 
            minVal=self.minVal(i) #find the smallest child of the root
            if self.data[i] > self.data[minVal]: #if the root is greater than the child, swap them
                temp = self.data[i]
                self.data[i]=self.data[minVal]
                self.data[minVal]= temp
            i=minVal #repeat for the new "root"

    def minVal(self,i):
        if i*2+1 > self.size: #if there is only a left node, return that node's position #
            return i*2
        else:
            if self.data[i*2] < self.data[i*2+1]: #else return the position # of the smaller item
                return i*2
            else:
                return i*2+1

    def dequeueMin(self):
        res = self.data[1]
        self.data[1] = self.data[self.size] # bring up the biggest value
        self.size -=1
        self.data.pop()
        self.reHeapDown(1)
        return res