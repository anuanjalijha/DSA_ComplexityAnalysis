def rotate(arr, n, d):
    arr1 = arr.copy()
    count = 0
    for i in range(d,n):
        arr[count] = arr[i]
        count+=1
    for i in range(d):
        arr[count] = arr1[i]
        count+=1
    return arr        
