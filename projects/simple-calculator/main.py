def calculate(left, operator, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return left / right
    if operator == "//":
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return left // right

    raise ValueError("Unsupported operator")


def main():
    left = float(input("First number: "))
    operator = input("Operator (+, -, *, /, //): ").strip()
    right = float(input("Second number: "))

    try:
        print(calculate(left, operator, right))
    except (ValueError, ZeroDivisionError) as error:
        print(error)


if __name__ == "__main__":
    main()
