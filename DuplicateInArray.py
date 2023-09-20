def findDuplicate(arr, n) :
    arr.sort()
    for i in range(0,n,1):
        if i==n-2 or arr[i]==arr[i+1]:
            return arr[i]
