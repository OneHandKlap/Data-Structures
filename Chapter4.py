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

print(revIt([1,2,2,3,4,5]))

def myAppend(x1,x2):
    if x2==[]:
        return x1
    else:
        return myAppend(x1+[x2[0]],x2[1:])

l1=[1,2,3,4,5]
l2=[5,4,3,2,1]

print("myAppend result:"+str(myAppend(l1,l2)))

def appendit(x1,x2):
    res=x1
    for i in range(len(x2)):
        res+=[x2[i]]
    return res

print("appendit result:"+str(appendit(l1,l2)))

def exponentialSeries(n,acc=0):
    if n==0:
        return acc
    else:
        acc=acc+n**n
        return exponentialSeries(n-1,acc)

n=4
print("exponentialSeries result:"+str(exponentialSeries(n)))

def palindromeCheck(string_list):
    if len(string_list)<=1:
        return True
    elif string_list[0]==string_list[len(string_list)-1]:
        return palindromeCheck(string_list[1:len(string_list)-1])
    else:
        return False

string="ablewasiereisawelba"
print("palindromeCheck result:"+str(palindromeCheck(string)))    
