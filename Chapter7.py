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
                

    # def __str__(self,acc=[],count=0,thisline=0):
    #     if self.getLeft()==None and self.getRight==None:
    #         acc.append(str(self.root)+"\t"+str(thisline))
    #         return acc
    #     else:
    #         count+=1
    #         thisline=count
    #         if acc[count]:
    #             acc[count].append("\n"+self.getLeft.__str__(acc,count))
    #             acc[count].append(self.getRight.__str__(acc,count)+"\t"+str(thisline))
    #         else:
    #             acc.append([])
    #             acc[count].append(self.getLeft.__str__(acc,count))
    #             acc[count].append(self.getRight.__str__(acc,count))

t=Tree(4)
t.addLeft('branch1')
t.addRight('branch2')
t.getLeft().addLeft('branch3')
t.getRight().addRight('branch4')

print (t.getSize())