def CheckPosition(arr,target,idx):
    List = []
    if idx > len(arr)-1:
        return List
       
    if arr[idx] == target:
       
       List.append(idx)
      
    if len(List ) > 0 :
        return CheckPosition(arr,target,idx+1)+List
    print("i am running the else")
    return CheckPosition(arr,target,idx+1)
  

print(CheckPosition([1,2,3,3,3,4,7],3,0))