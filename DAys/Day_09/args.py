def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

result = add_numbers(num1,num2,num3)

print("Total:",result)

