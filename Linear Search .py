def LinearSearch(arr,target,idx,arr2):
    if idx == len(arr):
        print("i am arr2",arr2)
        return arr2
    if arr[idx] == target:
        arr2.append(idx)
    return LinearSearch(arr,target,idx+1,arr2)
 
print(LinearSearch([1,2,3,3,3,4,5],1,0,[]))