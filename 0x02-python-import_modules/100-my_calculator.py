#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    ac = len(sys.argv) - 1
    if ac != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    if not sys.argv[1].isdigit() or not sys.argv[3].isdigit():
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    operator = sys.argv[2]
    if operator not in ('+', '-', '*', '/'):
        sys.stderr.write("Unknown operator. Available operators: "
                         "+, -, * and /\n")
        sys.exit(1)

    a = float(sys.argv[1]) if '.' in sys.argv[1] else int(sys.argv[1])
    b = float(sys.argv[3]) if '.' in sys.argv[3] else int(sys.argv[3])

    if operator == '+':
        print(f"{a} {operator} {b} = {calc.add(a, b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {calc.sub(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {calc.mul(a, b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {calc.div(a, b)}")
