try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

