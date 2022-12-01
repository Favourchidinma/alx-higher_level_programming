#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    ac = len(sys.argv) - 1
    if ac != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    if operator not in ('+', '-', '*', '/'):
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if operator == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calc.add(a, b)))
    elif operator == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calc.sub(a, b)))
    elif operator == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calc.mul(a, b)))
    elif operator == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calc.div(a, b)))
    sys.exit(0)
