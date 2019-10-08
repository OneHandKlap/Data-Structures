import timeit
import random

def groupElements(arr,res):
    if len(arr)==0:
        return res
    else:
        found=False
        if len(res)>0:
            for i in res:

                if arr[0] ==i[0]:
                    i.append(arr[0])
                    found=True
            if found == False:
                res.append([arr[0]])
        else:
            res.append([arr[0]])
        return groupElements(arr[1:],res)


# def search_dups(arr_of_strings):


def calc_string_score(string):
    res=0
    string_array=list(string)
    print(string_array)
    for i in range(len(string_array)):
        res+=ord(string_array[i])*(i+1)
    return res

def search_dups(arr_strings):
    vals=[]
    for i in arr_strings:
        k=hash()
    
print(groupElements([10,10,60,31,31,40,34,34,10],[]))
list=[random.randrange(0,100) for x in range(100)]
print(timeit.timeit("groupElements(list,[])", setup= "from __main__ import groupElements, list"))

#print(calc_string_score('heyman'))