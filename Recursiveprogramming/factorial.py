# Implement a the mathematical operation factorial with recursion

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial_helper(n):
    try:
        return factorial(n)
    except RecursionError:
        return None

print("Factorial of 6 is")
print(factorial_helper(6))

