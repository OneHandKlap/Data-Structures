def eval_tree(tree,env):
    try:
        if (tree[1]==[] or None) and (tree[2]==[] or None):
            return (tree[0])
        else:
            return eval_array([eval_tree(tree[0],env),eval_tree(tree[1],env),eval_tree(tree[2],env)],env)
    except(IndexError):
        return tree[0]
def eval_array(arr,env):
    operand_stack=[]
    operator_stack=[]
    operators=['*','/','+','-','!']
    def discover_operator(operator_char,operand1,operand2=0):
        try:
            if operator_char=='*':
                return operand1*operand2
            elif operator_char=='/':
                return operand1/operand2
            elif operator_char=='+':
                return operand1+operand2
            elif operator_char=='!':
                return factorial(operand1)
            else:
                return operand2-operand1
        except (TypeError,ZeroDivisionError):
            return None
    for x in range(len(arr)-1,-1,-1):
        if arr[x] in env:
            operand_stack.insert(0,env.get(arr[x]))
        elif arr[x] in operators:
            if not operator_stack:
                operator_stack.insert(0,arr[x])
            else:
                operator=operator_stack.pop(0)
                operand1=operand_stack.pop(0)
                operand2=operand_stack.pop(0)
                operand_stack.insert(0,discover_operator(operator,operand1,operand2))
                operator_stack.insert(0,arr[x])
        else:
            operand_stack.insert(0,arr[x])
    if operand_stack and operator_stack:
        operator=operator_stack.pop(0)
        operand1=operand_stack.pop(0)
        operand2=operand_stack.pop(0)
        operand_stack.insert(0,discover_operator(operator,operand1,operand2))

    return operand_stack.pop(0)
            

l=["*", ["/", ['+',['a'],['b']], ['c']], ["*", ['d'], ['e']]]
env=[['a',8],['b',9],['c',2],['d',12],['e',4]]
#print(dict(env))
print(eval_tree(l,dict(env)))

#print(eval_array(eval_tree(l),dict(env)))
        