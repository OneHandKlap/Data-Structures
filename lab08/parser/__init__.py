def precedence(oper):
    if oper in ['+', '-']:
        return 1
    else:
        return 2

def operatorp(x):
    return x in ['+', '-', '/', '*','!']

def numberp(x):
    return not operatorp(x)

def parse(expr):
    return parseHelper(expr, [], [])

def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    if isinstance(expr[0],list):
        return parseHelper(expr[1:],operators,[parseHelper(expr[0],[],[])]+operands)
    if numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        if expr[0]=='!':
            return ([expr[0],operands.pop(),[]])
        else:
            return parseHelper(expr[1:], [expr[0]]+operators, operands)
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])

#x=[['3','/','6'],'-', '9']
x=['3','/','(','(','6','-','9',')','+','1',')']
#x=[['4'], '+', ['3'], '+', '6']
#x="( 4 + 3 * 7 - 5 / ( 3 + 4 ) + 6 )"
print("--", parse(x))
#print("--", 	['-', ['/', ['3', [], []], ['!', ['6', [], []], []]], ['9', [], []]])

