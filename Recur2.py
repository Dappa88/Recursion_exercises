def NTriangel(n,Rows,columns):
    if Rows > n :
        return 
    if columns == Rows:
        print("*")
        NTriangel(n,Rows+1,1)
    else:
        print("*",end =" ")
         
        NTriangel(n,Rows,columns+1)
        
        
        
NTriangel(4,1,1)
     
     
