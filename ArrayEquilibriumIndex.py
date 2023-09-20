def arrayEquilibriumIndex(arr, n) :
    total_sum = 0
    i = 0 
    while i<len(arr):
        total_sum+=arr[i] 
        i+=1 
    left_sum = 0
    index = 0 
    while index<len(arr):
        right_sum = total_sum-left_sum-arr[index]
        if right_sum==left_sum:
            return index
        left_sum=left_sum+arr[index] 
        index+=1 
    return -1       