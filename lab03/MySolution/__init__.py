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
def check_valid(somestring):
    contains_operand=False
    contains_operator=False
    operators=['*','/','+','-']
    operands=['1','2','3','4','5','6','7','8','9','0']
    for char in somestring:
        if char in operands:
            contains_operand=True
        if char in operators:
            contains_operator=True
    if contains_operand and contains_operator:
        return True
    else:
        return False
def infixToPostfix(somestring):
    opstack= Stack()
    newString=[]
    operators=['*','/','+','-']
    if check_valid(somestring)==True:
        for char in somestring:
            try:
                char_int=int(char)
                newString.append(char)
            except:
                TypeError
                if char =='(':
                    opstack.push(char)
                elif char == ')':
                    temp=opstack.pop()
                    while temp!='(':
                        newString.append(temp)
                        temp=opstack.pop()
                else:
                    while (not opstack.isEmpty()):
                        if opstack.peek() in operators:
                            if operators.index(opstack.peek())<=operators.index(char):
                                temp = opstack.pop()
                                newString.append(temp)
                    opstack.push(char)
        while not opstack.isEmpty():
            newString.append(opstack.pop())
        return "".join(newString)
    else:
        return ('Invalid string')



def evaluate_postfix(somestring):
    operators = ['*','-','+','/']
    accumulator=Stack()
    def discover_operator(operator_char,operand1,operand2):
        if operator_char=='*':
            return operand1*operand2
        elif operator_char=='/':
            return operand1/operand2
        elif operator_char=='+':
            return operand1+operand2
        else:
            return operand1-operand2
    for char in somestring:
        try:
            char_int = int(char)
            accumulator.push(char_int)
        except:
            TypeError
            try:
                temp1=accumulator.pop()
                temp2=accumulator.pop()
                value = discover_operator(char,temp1,temp2)
                accumulator.push(value)
            except:
                IndexError
                return ('Invalid string')
    return accumulator


print(infixToPostfix('1+4*9'))