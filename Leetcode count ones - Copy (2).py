def countones(number,test,count):
    if number< test and test ==10:
       # countones(number,test,count+1)
        return count+1
   
    while number>=10:
        print("i am test",test)
        if test > number:
            print("i am the base condotion")
            print("i ak.count",count)
            
            return count
            
            
            
        
        if test == 10:
            print("i am here now",test)
            return countones(number,test+1,count+2)
        
        if test//10 ==1 and test%10 ==1:
           print("running now")
           return countones(number,test+1,count+2)
        elif test//10==1 and test%10 !=1:
           return countones(number,test+1,count+1)
  
 
countones(17,10,0)