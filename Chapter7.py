#Trees practice
class Tree():
    def __init__(self,data,parent=None):
        self.root=data
        self.parent=parent
        self.left=None
        self.right=None

    def addRight(self,data,parent=None):
        self.right=Tree(data,self)

    def addLeft(self,data,parent=None):
        self.left=Tree(data,self)

    def getNext(self):
        if self.parent!=None and self.parent.getRight() != self.root:
                return self.parent.getRight()
        else:
            return self.getLeft()
    def getLeft(self):
        return self.left
    def getParent(self):
        return self.parent
    def getRight(self):
        return self.right

    def getSize(self,count=0):
        if self.getLeft()==None and self.getRight()==None:
            return count
        else:
            count+=1
            if not self.getLeft():
                return self.getRight().getSize(count)
            elif not self.getRight():
                return self.getRight().getSize(count)
            else:
                return max(self.getRight().getSize(count),self.getRight().getSize(count))

    def printTree(self):
        treeDict=self.treeToDict()
        treeKeys=treeDict.keys()
        for i in range(max(treeKeys)+1):
            if i in treeKeys:
                print(str(i)+"\t"+str(treeDict[i])+"\n")
            else:
                print(str(i)+"\n")

    def treeToDict(self,dictionary={},count=0):
        if count==0:
            dictionary[count]=[self.root]
        if self.getLeft()==None and self.getRight()==None:
            return dictionary
        else:
            count+=1
            if not self.getLeft():
                if count in dictionary:
                    dictionary[count].append(self.getRight().root)
                else:
                    dictionary[count]=[self.getRight().root]
                return self.getRight().treeToDict(dictionary,count)
            elif not self.getRight():
                if count in dictionary:
                    dictionary[count].append(self.getLeft().root)
                else:
                    dictionary[count]=[self.getLeft().root]
                return self.getLeft().treeToDict(dictionary,count)
            else:
                if count in dictionary:
                    
                    dictionary[count].append(self.getLeft().root)
                    dictionary[count].append(self.getRight().root)
                else:
                    dictionary[count]=[self.getLeft().root]
                    dictionary[count].append(self.getRight().root)
                self.getLeft().treeToDict(dictionary,count)
                self.getRight().treeToDict(dictionary,count)
                return dictionary

    def getTreeQueue(self,queue=[]):
        if self.getLeft()==None and self.getRight()==None:
            queue.append(self.root)
            return queue
        else:
            if not self.getLeft():
                queue.append(self.root)
                return self.getRight().getTreeQueue(queue)
            elif not self.getRight():
                queue.append(self.root)
                return self.getRight().getTreeQueue(queue)
            else:
                queue.append(self.root)
                self.getLeft().getTreeQueue(queue)
                self.getRight().getTreeQueue(queue)
                return queue
    
    # def printTree2(self):
    #     size = self.getSize()
    #     print("\t"*size+str(self.root))
    #     treeDict=self.treeToDict()
    #     treeKeys=treeDict.keys()
    #     treeQueue=self.getTreeQueue
    #     for i in range(size+1):







t=Tree(0)
b=Tree(1)
c=Tree(2)
d=Tree(3)
t.addLeft(1,t)
t.addRight(2,t)
t.getLeft().addLeft(11,t.getLeft())
t.getRight().addRight(22,t.getRight())
t.getRight().addLeft(21,t.getRight)
t.getLeft().addRight(12,t.getLeft())
print(t.getNext().getNext().parent.getRight().root)