def Cyclic(arr,index):
    while index < len(arr):
        value = arr[index]-1
        if index != arr[index]-1:
            arr[index],arr[value] = arr[value],arr[index]
        else:
            index +=1
    return arr
     
print(Cyclic([3,5,2,1,4],0))
            
            
            
            
 
            
    