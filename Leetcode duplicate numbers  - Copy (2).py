def Duplicate(arr,index):
    if index == len(arr):
        return arr
    if index>0:
        value = arr[index]
        if arr[index] == arr[value]:
            return Duplicate(arr,index+1)
        else:
            value = arr[index]
            arr[index],arr[value] = arr[value],arr[index]
            return Duplicate(arr,index)
    else:
        if arr[index] == 1:
            return Duplicate(arr,index+1)
        else:
            arr[index],arr[index+1] = arr[index+1],arr[index]
            return Duplicate(arr,index)
print(Duplicate([1,2,3,1],0))
            
            
def returnDuplicate(arr):
            arr = Duplicate(arr,0)
            for i in range(1,len(arr)):
                value = arr[i]
                if i == 1 or i == arr[value]:
                    return arr[i]
            
print(returnDuplicate([1,2,3,3]))
            