def RecurCyclic(arr,index):
    Value = index +1
    if index > len(arr)-1:
        return arr
    if index == arr[index]-1:
        return RecurCyclic(arr,index+1)
    else:
        Value = arr[index]
        
        print(" i am index now",arr[index]-1)
        arr[index],arr[Value-1]= arr[Value-1],arr[index]
        print("i am array now",arr)
        return RecurCyclic(arr,index)
        
   
print(RecurCyclic([5,4,3,2,1],0))
    