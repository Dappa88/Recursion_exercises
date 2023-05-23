def MissingNumbers(arr,index):
    while index < len(arr):
        if index == len(arr)-1:
             arr2 =[]
             for i in range(0,len(arr)):
                 if i +1 != arr[i]:
                     arr2.append(i+1)
             return arr2
             
            #while True:
                #if inde
                
            
            
             #return arr
         
        value = arr[index]
        if value  == arr[value-1]:
            index+=1
        else:
            value =arr[index]
            
            arr[index] ,arr[value -1]=arr[value -1],arr[index]
           
            
            
print(MissingNumbers([4,3,2,7,8,2,3,1],0))
            