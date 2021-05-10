# Multiplication using only + and -

def mul_rec(a, b):
    if b < 1:
        return 0
    else:
        return a + mul_rec(a, b-1)


def multiply(a, b):
    try:
        return mul_rec(a, b)
    except RecursionError:
        return None


if __name__ == '__main__':
    print("This is from Recursion!!!!")
    print(multiply(18, 200))
