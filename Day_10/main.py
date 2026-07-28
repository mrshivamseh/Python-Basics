import math_operations

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))

result1 = math_operations.add(num1,num2)
result2 = math_operations.subtract(num1,num2)

print("Addition:",result1)
print("Subtraction:",result2)

print("\n")
print("New program:2")
print("\n")

from math_operations import add

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))

result = add(num1,num2)

print("Addition:",result)


print("\n")
print("New program:3")
print("\n")

from math_operations import add,subtract

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))

addition = add(num1,num2)
subtraction = subtract(num1,num2)

print("Addition:",addition)
print("Subtraction:,subtraction")



