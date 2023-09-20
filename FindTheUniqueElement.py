def findUnique(arr, n) :
    arr.sort()
    for i in range(0,n,2):
        if i==n-1 or arr[i]!=arr[i+1]:
            return arr[i]
