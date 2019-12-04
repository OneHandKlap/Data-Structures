class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size=0
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def place(self,key,val):
        if self.root:
            self.put(key,val,self.root)
        else:
            self.root = Node(key,val)
        self.size+=1
    def put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeft():
                self.put(key,val,currentNode.left)
            else:
                currentNode.left = Node(key,val,parent=currentNode)
        else:
            if currentNode.hasRight():
                self.put(key,val,currentNode.right)
            else:
                currentNode.right = Node(key,val,parent=currentNode)
    def __setitem__(self,key,val):
        self.place(key,val)
    def get(self,key):
        if self.root:
            res = self.retrieve(key,self.root)
            if res:
                return res.val
            else:
                return None
    def retrieve(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return retrieve(key,currentNode.getLeft())
        else:
            return retrieve(key,currentNode.getRight())
    def __getitem__(self,key):
        return self.get(key)
 
class Node():
    def __init__(self, key, val, left=None,right=None,parent=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
    def hasLeft(self):
        return self.left
    def hasRight(self):
        return self.right
    def isLeft(self):
        return self.parent and self.parent.left ==self
    def isRight(self):
        return self.parent and self.parent.right==self
    def isRoot(self):
        return not self.parent
    def hasBoth(self):
        return self.right and self.left
    def replaceData(self, key,val,left,right):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        if self.hasLeft():
            self.left.parent=self
        if self.hasRight():
            self.right.parent=self
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def inorder(self):
        if self.hasLeft():
            self.getLeft().inorder()
        print(self.val)
        if self.hasRight():
            self.getRight().inorder()