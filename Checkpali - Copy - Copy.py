

def Pali(str):
    if len(str) ==1:
        return str
     
    rest = str[0:len(str)-1]
    print("rest",rest)
    return str[len(str)-1] + Pali(rest)

def CheckPali(str):
    if str == Pali(str):
        return True
    return False
     
     
     
print(CheckPali("racecar"))
       
    