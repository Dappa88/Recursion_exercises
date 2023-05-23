def RemoveA(str):
    rest = str[1:len(str)]
    if len(rest) ==1:
        if rest[0] != "a":
            return rest[0]
        else:
             return ""
    if str[0] =="a":
        return RemoveA(str[1:len(str)])
        
    else:
        return str[0] + RemoveA(rest)
       
      
print(RemoveA("baccad"))