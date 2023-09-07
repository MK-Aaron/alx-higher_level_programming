#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    import sys
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])

    if sign == '+':
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign == '-':
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign == '*':
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign == '/':
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
