def bubble_sort(arr):
    for i in range(len(arr)-1):
        print(i)
        swapped_items=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                swapped_items=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if swapped_items==False:
            return arr
    return arr

# l=[3,9,3,4,6,5]
# print(bubble_sort(l))

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

# l=[3,9,3,4,6,5]
# print(recursive_bubble_sort(l))

def selection_sort(arr):
    for j in range(len(arr)):
        print("pass number:"+str(j))
        swap_items=False
        largest_index=0
        for i in range(len(arr)-j):
            print("item number:"+str(i))
            if arr[i]>arr[largest_index]:
                largest_index=i
                swap_items=True
        if swap_items:
            #print(arr[len(arr)-1-j])
            arr[len(arr)-1-j],arr[largest_index]=arr[largest_index],arr[len(arr)-1-j]
    return arr

l=[3,9,3,4,6,5]
print(selection_sort(l))
        