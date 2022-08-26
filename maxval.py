def countingSort(array):
    size=len(array)
    output=[0]*size
    
    count=[0]*10
    
    for i in range(0,size):
        count[array[i]]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=size-1
    while i>=0:
        output[count[array[i]]-1]=array[i]
        count[array[i]]-=1
        i-=1
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
        















'''
a=[1,2,4,3]
max=0
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
val=[0]*(max + 1)
print(val)
for j in range(0,len(val)):
    for x+1 in range(0,len(a)):
        if()
    '''