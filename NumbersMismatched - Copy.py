def Mismatch(arr,index):
    if index == len(arr)-1:
        return arr
    if index+1 == arr[arr[index]-1]:
        return Mismatch(arr,index+1)
    else:
        value =arr[index]-1
        
        if arr[value]== arr[index]:
            return Mismatch(arr,index+1)
        else:
            arr[index],arr[value] = arr[value],arr[index]
            print("i am arr",arr)
            print("index",index)
            return Mismatch(arr,index)
       
       
       
def ReturnMismatch(arr):
   arr2 =[]
   arr = Mismatch(arr,0)
   for i in range(0,len(arr)):
       if arr[i] != i+1:
           arr2.append(arr[i])
           arr2.append(i +1)
          
           
   return arr2
   
   
print(ReturnMismatch([1,1]))
   