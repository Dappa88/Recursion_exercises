
noOfZero = 0

def countZero(num):
    global noOfZero
    
    if num < 10 :
        if num ==0:
            noOfZero+=1
        else:
            return noOfZero
    
    if num % 10 ==0:
        noOfZero +=1
        countZero(num//10)
    else:
        countZero(num//10)

        

print(countZero(109))