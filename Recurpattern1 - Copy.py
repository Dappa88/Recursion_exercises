def RecurPattern(Row,Column):
    if Row ==0:
        return
       
    if Column == Row :
        print("*")
        RecurPattern(Row-1,0)
       
    if Column < Row:
        if Column > 0:
            print("*",end =" ")
            RecurPattern(Row,Column +1)
        else:
            RecurPattern(Row,Column +1)
       
RecurPattern(4,0)