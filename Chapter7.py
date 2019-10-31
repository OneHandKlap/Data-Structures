#Trees practice
class Tree():
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

    def addRight(self,data):
        self.right=Tree(data)

    def addLeft(self,data):
        self.left=Tree(data)

    def getLeft(self):
        return self.left
    
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





t=Tree(0)
t.addLeft(1)
t.addRight(2)
t.getLeft().addLeft(11)
t.getRight().addRight(21)
t.getRight().addLeft(22)
t.getLeft().addRight(12)
t.printTree()