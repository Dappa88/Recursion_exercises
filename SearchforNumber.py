def Recur(arr,target,idx):
    if idx > len(arr)-1:
        return -1
    if arr[idx] == target:
        return idx
    return Recur(arr,target,idx+1)
    
    
print(Recur([1,2,3,4,5],2,0))
    