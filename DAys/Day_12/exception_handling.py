try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter secound number:"))

    result = num1/num2

    print("Result:",result)

except ZeroDivisionError:
    print("You cannot divide by zero.")

    