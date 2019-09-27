def sort(list):
    smallAcc=[]
    bigAcc=[]
    if list==[]:
        return smallAcc+bigAcc
    else:
        smallerOnes=thoseSmallerThan(list[0],list[1:],smallAcc)
        biggerOnes=thoseBiggerThan(list[0],list[1:],bigAcc)
        return sort(smallerOnes)+[list[0]]+sort(biggerOnes)

def thoseSmallerThan(num,list,acc):
    if list==[]:
        return acc
    elif num>list[0]:
        acc.append(list[0])
        return thoseSmallerThan(num,list[1:],acc)
    else:
        return thoseSmallerThan(num,list[1:],acc)

def thoseBiggerThan(num,list,acc):
    if list==[]:
        return acc
    elif num<=list[0]:
        acc.append(list[0])
        return thoseBiggerThan(num,list[1:],acc)
    else:
        return thoseBiggerThan(num,list[1:],acc)
  
            
l=[8,5,9,3,10,7,3,2,2,0]
bigAcc=[]
print(sort(l))


#Use Recursion when supported by the underlying data-structure. Binary trees for example

def rev(x):
    if x==[]:
        return []
    else:
        return rev(x[1:]+[x[0]])

def revIt(x):
    acc=[]
    for i in range(len(x)):
        acc.append(x[len(x)-1-i])
    return acc

print(rev([1,2,2,3,4,5]))
print(revIt([1,2,2,3,4,5]))