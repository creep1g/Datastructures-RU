# Sum of digits in positive integers

def sum_of_digits(x):
    if x < 10:
        return x
    else:
        digit = x % 10
        remainder = x // 10

    return digit + sum_of_digits(remainder)


print(sum_of_digits(1234))
