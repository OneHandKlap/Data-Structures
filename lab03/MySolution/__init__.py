#Basic Stack implementation
class Stack():

    def __init__(self):
        self.data_list=[]
    def get_data(self):
        return self.data_list
    def push(self, data):
        self.data_list.insert(0,data)
    def pop(self):
        return self.data_list.pop(0)
    def __str__(self):
        return str(self.get_data())

    def peek(self):
        return self.data_list[0]

    def isEmpty(self):
        if len(self.data_list)==0:
            return True
        else:
            return False

#Deprecated check_valid function that verifies the correct number of operators and operands in a given string.
# def check_valid(somestring):
#     contains_operand=0
#     contains_operator=False
#     operators=['*','/','+','-','!']
#     operands=['1','2','3','4','5','6','7','8','9','0']
#     contains_factorial=False
#     for char in somestring:
#         if char =='!':
#             contains_factorial=True
#         if char in operands:
#             contains_operand+=1
#         if char in operators:
#             contains_operator=True
#     if contains_operand>=2 and contains_operator or (contains_operand>=1 and contains_factorial):
#         return True
#     else:
#         return False

#My conversion function, that takes in a string of single spaced characters and converts it to postfix notation
def infixToPostfix(somestring):
    opstack= Stack()
    newString=[]
    operators=['*','/','+','-','!','(']
    operator_precedence={'*':3,'/':3,'+':2,'-':2,'(':1,'!':1}
    # if check_valid(somestring)==True:
    for char in somestring:
        if char in "0123456789":
            newString.append(char)
        elif char =='(':
            opstack.push(char)
        elif char =='!':
            newString.append(char)
        elif char == ')':
            temp=opstack.pop()
            while temp!='(':
                newString.append(temp)
                temp=opstack.pop()
        else:
            while (not opstack.isEmpty()) and (operator_precedence.get(opstack.peek())>=operator_precedence.get(char)):
                temp = opstack.pop()
                newString.append(temp)
            opstack.push(char)
    while not opstack.isEmpty():
        newString.append(opstack.pop())
    return "".join(newString)

#My postfix evaluator function that takes in somestring in postfix notation and performs the requisite mathematical operations on it to provide a sum
def evaluate_postfix(somestring):
    operators = ['*','-','+','/','!']
    accumulator=Stack()
    def discover_operator(operator_char,operand1,operand2=0):
        if operator_char=='*':
            return operand1*operand2
        elif operator_char=='/':
            return operand2/operand1
        elif operator_char=='+':
            return operand1+operand2
        elif operator_char=='!':
            return factorial(operand1)
        else:
            return operand2-operand1
    # if check_valid(somestring):
    for char in somestring:
        try:
            char_int = int(char)
            accumulator.push(char_int)
        except:
            TypeError
            try:
                if char =='!':
                    temp1=accumulator.pop()
                    accumulator.push(factorial(temp1))
                else:
                    temp1=accumulator.pop()
                    temp2=accumulator.pop()
                    value = discover_operator(char,temp1,temp2)
                    accumulator.push(value)
            except:
                IndexError
    return accumulator.pop()

#custom recursive factorial helper function... style points?
def factorial(number):
    if number==0:
        return 1
    while number>0:
        return number*factorial(number-1)
