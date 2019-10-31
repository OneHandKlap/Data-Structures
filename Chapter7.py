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

    def __str__(self):
        if self.getLeft()==None and self.getRight()==None:
            print (str(root))
        else:
            res=[]
            res.append((self.getLeft().__str__()))
            res.append((self.getRight().__str__()))
            print(str(res))

t=Tree(4)
t.addLeft('branch1')
t.addRight('branch2')
t.getLeft().addLeft('branch3')
t.getRight().addRight('branch4')

t.__str__()