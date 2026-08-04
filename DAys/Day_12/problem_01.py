try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    operation = input("Enter operation(+,-,*,/):")

    if operation == "+":
        print("Result:",num1 + num2)

    elif operation == "-":
        print("Result:",num1 - num2)

    elif operation == "*":
        print("Result:",num1*num2)

    elif operation == "/":
        print("Result:",num1/num2)

    else:
        print("Invalid operation.")


except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

finally:
    print("Calculater closed.")

    