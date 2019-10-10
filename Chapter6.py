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

l=[3,9,3,4,6,5]
print(bubble_sort(l))