def sortArray(arr):
    n = len(arr)
    if n == 1: return arr
    for i in range(1, n):
        j=i-1
        tmp=arr[i]
        while j>=0 and arr[j]>tmp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=tmp
    return arr
res=sortArray([5,2,3,1])
print(res)