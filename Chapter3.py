
from pythonds.basic import Stack

def divideby2(number):
    remainderstack = Stack()
    
    while number>0:
        
        remainderstack.push(number%2)
        number = number//2

    binary_string=''
    while not remainderstack.isEmpty():
        binary_string+=str(remainderstack.pop())
    
    return binary_string

def baseConvert(number, base):
    digits='0123456789ABCDEF'

    remainderstack = Stack()

    while number>0:
        remainder = number%base
        remainderstack.push(remainder)
        number=number//base

    string=''
    while not remainderstack.isEmpty():
        string+= digits[(remainderstack.pop())]
    return string

print(baseConvert(26,26))