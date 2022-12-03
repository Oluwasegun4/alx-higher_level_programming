#!/usr/bin/python3
from calculator_1 import mul, sub, add, div
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
for i in range(args):
    a = int(sys.argv[1])
    operator = (sys.argv[2])
    b = int(sys.argv[3])
if operator == "+":
    print("{} {} {} = {}".format(a, operator, b, add(a, b)))
elif operator == "*":
    print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
elif operator == "-":
    print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
elif operator == "/":
    print("{} {} {} = {}".format(a, operator, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
