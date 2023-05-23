def MissingNumber(arr,index):
    value = index
    if index > len(arr):
        return -1
    if value in arr:
        return MissingNumber(arr,index+1)
    return value
    
print(MissingNumber([9,5,4,1,3,2,0,6],0))