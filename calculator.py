def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def powers(a, b):
    b = int(b)
    value = a
    for i in range(b - 1):
        value = value * a
        i = i + 1
    return value

def circleArea(r):
    if r >= 0:
        return 3.14 * r * r
    else:
        return "NaN"

def circleCircumference(d):
    if d >= 0:
        return 3.14 * d
    else:
        return "NaN"


def main():
    while True:
        a = float(input("First number: "))
        op = input("Operator (+ - * / ^): ")
        b = float(input("Second number: "))

        if op == "+":
            print("Result: ", add(a,b))
        elif op == "-":
            print("Result: ", subtract(a,b))
        elif op == "*":
            print("Result: ", multiply(a,b))
        elif op == "/":
            print("Result: ", divide(a,b))
        elif op == "^":
            print("Result: ", powers(a,b))
        else:
            print("Unknown operator: ", op)

if __name__ == "__main__":
    main()
