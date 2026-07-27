def multiply_numbers(*numbers):
    result = 1

    for number in numbers:
        result = result*number

    return result


num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

answer = multiply_numbers(num1,num2,num3)

print("Multiplication:",answer)

