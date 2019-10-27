import statistics
import timeit
import random
import matplotlib.pyplot as plt

def quickSort(alist,mo3=False):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last,mo3=False):
    
    if first<last:

        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1,mo3)
        quickSortHelper(alist,splitpoint+1,last,mo3)

def partition(alist,first,last,mo3=False):
    pivotvalue=alist[first]
    if mo3:
        pivotvalue = statistics.median([alist[first],alist[last],alist[int((last-first)/2)+first]])
    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark


lengths=[x for x in range(0,50000,5000)]
quick=[]
quick_mo3=[]

for length in lengths:
    arr=[random.randrange(100) for x in range(length)]
    quickSort_temp=[]
    quickSort_mo3_temp=[]
    for i in range(3):
        quickSort_temp.append((timeit.timeit("quickSort(arr)", setup = "from __main__ import quickSort,arr", number = 1)))
        quickSort_mo3_temp.append((timeit.timeit("quickSort(arr,True)", setup = "from __main__ import quickSort,arr", number = 1)))
    quick.append(statistics.mean(quickSort_temp))
    quick_mo3.append(statistics.mean(quickSort_mo3_temp))
print(quick)
print(quick_mo3)

plt.plot(lengths,quick,'ro', label = "quickSort canon results")
plt.plot(lengths,quick_mo3, 'bo', label = "quickSort mo3 results")
plt.xlabel("Number of Elements")
plt.ylabel("Timeit Values")
plt.legend(loc='upper left')
plt.show()