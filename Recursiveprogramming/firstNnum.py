# Print the first n natural numbers using recursion

def print_naturals(n):
    if n < 1:
        return 1
    else:
        print_naturals(n-1)
        print(n, end=" ")


print_naturals(20)
