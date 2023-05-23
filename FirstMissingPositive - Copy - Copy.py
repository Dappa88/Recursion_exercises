def MissingPositive(arr,index):
    if index == len(arr)-1:
        return arr
       
    if arr[index]>0:
        value = arr[index]-1
        if arr[index] == index +1:
            return MissingPositive(arr,index+1)
        if arr[value] == arr[index]:
            return MissingPositive(arr,index+1)
        else:
            arr[index],arr[value] =arr[value],arr[index]
            return MissingPositive(arr,index)
    else:
        return MissingPositive(arr,index+1)
       
def ReturnMissingPositive(arr):
    arr = MissingPositive(arr,0)
    for i in range(0,len(arr)):
        if (i +1) != arr[i]:
            return i+1
print(MissingPositive([7,8,9,10,12],0))