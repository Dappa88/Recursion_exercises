def Allduplicates(arr,index):
    arr2 = []
    while index < len(arr):
        if index == len(arr) -1:
            return arr
        if arr[index] == index +1:
          
          
          
          index+=1
          
          
          
          
        else:
            print("i am index",index)
            
            if arr[arr[index]-1] == arr[index]:
                value = arr[index]
                print("i am arr[index]",arr[index])
                arr2.append(value)
                
                
               
                
                
                index +=1
            else:
               value = arr[index]
               arr[index],arr[value-1] = arr[value-1],arr[index]
               
               
def ReturnDuplicates(arr):
               arr2 =[]
               arr = Allduplicates(arr,0)
               for i in range(0,len(arr)):
                   if arr[i] != i +1:
                       arr2.append(arr[i])
               return arr2
print(ReturnDuplicates([4,3,2,7,8,2,3,1]))
               
              
            
           
            
           
            