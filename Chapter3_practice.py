#practice building a linked list from scratch
from pythonds.basic import Stack
class Node():

    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data=new_data

    def set_next(self, node):
        self.next=node

class Unordered_list():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def __str__(self):
        temp=[]
        current = self.head
        while current!=None:
            temp.append(current.get_data())
            current=current.get_next()
        return str(temp)

    def size(self):
        current = self.head
        count= 0 
        while current != None:
            count+=1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found=False
        while current!=None and found==False:
            if current.get_data()==item:
                found=True
                break
            else:
                current=current.get_next()
        return found
        
    def remove(self,item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.get_data()==item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

def convertBinary(num, stack=Stack()):
    if num ==0:
        res=""
        while not (stack.isEmpty()):
            res+=str(stack.pop())
        return res
    else:
        stack.push(num%2)
        convertBinary(num//2,stack)

print(convertBinary(1132))