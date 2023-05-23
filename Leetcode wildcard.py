def Wilcard(s,p,index):
    if index == len(p) and index  < len(s):
        print("i am here",index)
        return False
    if index >= len(p) and index >=len(s):
        return True
    if p[index] != "*" and  p[index] !="?":
        print("i am here oo")
        return False
    if p[index] == "*":
        return True
    if p[index] == "?":
       return Wilcard(s,p,index+1)
       
       
print(Wilcard("aa","a",0))
     
       