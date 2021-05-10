# problem 1.1

def sum_num(a, b):
    return a + b


def get_input():
    num12 = input("Enter two integers to be summed seperated by a comma [1,3]: ")
    num1, num2 = num12.split(",")
    return (int(num1), int(num2))


# Problem 1.2

def calc_area(a):
    return a * a


def main():
    num1, num2 = get_input()
    print(sum_num(num1, num2))
    side = input("Enter a singleside of a square: ")
    print(calc_area(int(side)))


if __name__ == "__main__":
    main()
