def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call


dispn(5)

