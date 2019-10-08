import timeit

def groupElements(arr,res):
    if len(arr)==0:
        return res
    else:
        if len(res)>0:
            for i in res:
                found=False
                if arr[0] in i:
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
        print(string_array)
        res+=ord(string_array[i])*(i+1)
    return res

    
# print(groupElements([10,10,10,31,31,40,34,34,60],[]))
# list=[10,10,10,31,31,40,31,34,60]
# print(timeit.timeit("groupElements(list,[])", setup= "from __main__ import groupElements, list"))

print(calc_string_score('heyman'))