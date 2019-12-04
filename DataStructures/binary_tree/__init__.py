class BinaryTree:
    def __init__(self, root):
        self.key=root
        self.left=None
        self.right=None

    def insertLeft(self,new):
        if self.left==None:
            self.left = BinaryTree(new)
        else:
            newLeft=BinaryTree(new)
            newLeft.left,self.left=self.left,newLeft
    def insertRight(self,new):
        if self.right==None:
            self.right = BinaryTree(new)
        else:
            newRight=BinaryTree(new)
            newRight.right,self.right=self.right,newRight
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRoot(self,data):
        self.key=data
    def getRoot(self):
        return self.key
def preorder(tree):
    if tree:
        print(tree.getRoot())
        preorder(tree.getLeft())
        preorder(tree.getRight())
def postorder(tree):
    if tree != None:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.getRoot())
def inorder(tree):
      if tree != None:
        inorder(tree.getLeft())
        print(tree.getRoot())
        inorder(tree.getRight())
    
class Stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
    def __pop__():
        self.pop(0)

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeft()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRoot(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRight()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRoot(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree
import operator
def eval(parsedTree):
    operators = {'+':operator.add,'-':operator.sub,'/':operator.truediv,'*':operator.mul}
    left=parsedTree.getLeft()
    right=parsedTree.getRight()

    if left and right:
        op = operators[parsedTree.getRoot()]
        return op(eval(left),eval(right))
    else:
        return parsedTree.getRoot()


