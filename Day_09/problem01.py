def find_largest(*numbers):
    return max(numbers)




num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

result = find_largest(num1,num2,num3)

print("Largest number:",result)


