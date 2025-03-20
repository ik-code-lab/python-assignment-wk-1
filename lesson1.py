operator = input("Enter an operator (+ - * /)")
number1 = float(input("Enter the first nunber:"))
number2 = float(input("Enter the second nunber:"))

if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(result)
else:
    print(f"{operator} is not a valid operator")


