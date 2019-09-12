import matplotlib.pyplot as plt
import time
def sumofN1(n):
    the_sum=0
    for i in range(1,n+1):
        the_sum+=i
    return the_sum

#print(sumofN1(10))

#Algorithm analysis
#   - readability
#   -performance (computing resources)
#       -memory andd time

def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
        fred = fred+bill
    return fred

def sumof(n):
    return (n*(n+1)/2)

sumofN1_times=[]
foo_times=[]
sumof_times=[]
index = [i for i in range(100)]
for i in range(100):
    i=i*100
    start_time=time.time()
    sumofN1(i)
    sumofN1_times.append(round(time.time()-start_time,10))

    start_time=time.time()
    foo(i)
    foo_times.append(time.time()-start_time)

    start_time=time.time()
    sumof(i)
    sumof_times.append(time.time()-start_time)

print (sumofN1_times)
plt.subplots()
ax1=plt.plot(index,sumofN1_times,'--r',index,foo_times,'g^',index,sumof_times,'bs')
plt.show()
        
#Big-O notation, Order of magnitude
# efficiency of an algorithm is determined by the largest degree
#example function T(n)=5n^2+27n has an order of magnitude of O(n^2)