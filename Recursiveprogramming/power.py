def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)


if __name__ == '__main__':
    user_input = ""

    while user_input != "q":
        try:
            user_input = input("Please enter two numbers(base, exp): ")
            base, exp = user_input.split(", ")
            print(power(int(base), int(exp)))
        except RecursionError:
            print("Exponent {} was to high".format(exp))
    print("Thanks!")
