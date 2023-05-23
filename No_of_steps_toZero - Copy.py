Count_Steps =0
def Steps(num):
    global Count_Steps
    if num == 0:
        print(" i am steps now",Count_Steps)
        return Count_Steps
    if num %2 ==0:
        Count_Steps +=1
        
        Steps(num/2)
    else :
        num -=1
        Count_Steps +=1
        Steps(num)
        
Steps(14)
        

        
        
        
        
        