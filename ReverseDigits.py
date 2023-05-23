def reverse(N):
    N = str(N)
    if len(N) == 1:
        return N
    rest = N[0:len(N)-1]
    return N [len(N)-1] + reverse(rest)
    
    
print(reverse(12345))
    