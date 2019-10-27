def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped_items=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                swapped_items=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if swapped_items==False:
            return arr
    return arr


def recursive_bubble_sort(arr,flag=True,count=0):
    if flag==False:
        return arr
    else:
        flag=False
        for i in range(count,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                flag = True
        count+=1
        return recursive_bubble_sort(arr,flag,count)


def selection_sort(arr):
    for j in range(len(arr)):
        swap_items=False
        largest_index=0
        for i in range(len(arr)-j):
            if arr[i]>arr[largest_index]:
                largest_index=i
                swap_items=True
        if swap_items:
            arr[len(arr)-1-j],arr[largest_index]=arr[largest_index],arr[len(arr)-1-j]
    return arr

def recursive_sel_sort(arr,flag=True,count=0):
    if flag==False or count==len(arr):
        return arr
    else:
        flag==False
        largest=max(arr[:len(arr)-count])
        index_largest=arr.index(largest)
        arr[len(arr)-1-count],arr[index_largest]=arr[index_largest],arr[len(arr)-1-count]
        flag=True
        count+=1
        return (recursive_sel_sort(arr,flag,count))

l=[3,9,3,4,6,5]
print(recursive_sel_sort(l))


def josephus(num_prisoners,num_candy,start_pos):
    end_pos=(num_candy%num_prisoners)+start_pos-1
    print(end_pos)
    if end_pos<num_prisoners:
        
        return end_pos
    else:
        return end_pos-num_prisoners-1


print(josephus(352926151 ,380324688 ,94730870))

def insertion_sort(arr):
    for i in range(len(arr)):
        local_min=min(arr[i:])
        arr.remove(local_min)
        arr.insert(i,local_min)    
    return arr
def recursive_insertion_sort(arr,acc=[]):
    if arr==[]:
        return acc
    else:
        acc.append(min(arr))
        arr.remove(min(arr))
        return(recursive_insertion_sort(arr,acc))

# l=[6,5,3,2,1]
# print(insertion_sort(l))
