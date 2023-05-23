def RemoveA(str,index):
    if index==len(str):
        return str
       
    if str[index] =="a" or str[index] == "A":
        str = str.replace(str[index],"")
        return RemoveA(str,index+1)
        
    else:
        return RemoveA(str,index+1)
        
print(RemoveA("baccad",0))
        