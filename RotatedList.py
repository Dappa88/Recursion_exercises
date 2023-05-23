def RotatedList(arr,start,end):
    mid = (start +end)//2
    if start == end:
        return -1
    if arr[mid]< arr[mid-1] and arr[mid]<arr[mid+1]:
        return mid
    if arr[mid] > arr[mid-1] and arr[mid] < arr[mid +1]:
        return RotatedList(arr,start,mid-1)
    return RotatedList(arr,mid-1,end)
    
    
print(RotatedList([4,5,1,2,3],0,4))
    
    
    