# Implement a recursive function that returns a fibonacci lnumber

def fibbo(n):
    '''Returns a tuple of fibonacci(n) and fibonacci(n-1). from the book'''
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibbo(n-1)
        return (a+b, a)


def fib(n):
    '''Returns fibonacci number n'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_helper(n, 0, 1, 3)


def fib_helper(n, a, b, i):
    '''Helper for fib(n)'''
    if i == n:
        return a + b
    temp = b 
    b = b + a
    a = temp
    return fib_helper(n, a, b, i+1)

# non recursive
def fobo(n):
    one = 0
    two = 1
    temp = 0
    for i in range(n - 1):
        print(temp)
        if temp == 0:
            print(1)
        temp = one + two
        one = two
        two = temp
   

print(fib(10))
