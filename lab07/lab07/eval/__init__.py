def eval_tree(tree,env):
    env=dict(env)
    try:
        if (tree[1]==[] or None) and (tree[2]==[] or None):
            return (tree[0])
        else:
            return eval_array_2([eval_tree(tree[0],env),eval_tree(tree[1],env),eval_tree(tree[2],env)],env)
    except(IndexError):
        return tree[0]
def eval_array_2(arr,env):
    operator = arr[0]
    if arr[1] in env:
        operand1=env.get(arr[1])
    else:
        operand1=arr[1]
    if arr[2] in env:
        operand2=env.get(arr[2])
    else:
        operand2=arr[2]
    try:
        return eval(str(operand1)+str(operator)+str(operand2))
    except:
        return None

l=["/", ["*", ["a", [], []], ["b", [], []]], ["*", ["c", [], []], ["d", [], []]]]
env=[["a", 10], ["b", 9], ["c", 5], ["d", 10], ["e", 8]]
#print(dict(env))
print(eval_tree(l,dict(env)))

#print(eval_array(eval_tree(l),dict(env)))
