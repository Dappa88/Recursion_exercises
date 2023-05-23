def RecurMissing(arr,index):
    if index==len(arr)-1:
        return arr
       
    
    if arr[index] == arr[arr[index]]:
         return RecurMissing(arr,index+1)
    else:
          value = arr[index]
          print("i am arr",arr[index])
          arr[index], arr[value]=arr[value],arr[index]
          print("i am arr2",arr[index])
          return RecurMissing(arr,index)
         
     
    
def MissingNumber(arr,index):
      arr = RecurMissing(arr,0)
      #return arr
      #print("i am index now",index)
      while True:
          
          if arr[index] !=index:
              return index
          else:
              #print("i am array",arr)
              index += 1
              if index > len(arr)-1:
                  return len(arr)
          
  
  
              
          
#print(MissingNumber([3,1,0],0))
 
#print(len([9,8,6,5,4,3,2,1,0]))
      
     
print(RecurMissing([2,1,0,3],0))

#print(RecurMissing([0,1,2,3,4],0))