def String(str):
            if len(str) == 1:
                return int(str)
            rest = str[1:]
            return int(str[0])+ String(rest)
            
            
     
print(String("14000"))
            
        
    