from calculator import add as addition
from calculator import subtract as subtraction
from calculator import multiplication
from calculator import division

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))

print("Addition:",addition(num1,num2))
print("Subtraction:",subtraction(num1,num2))
print("Multiplication:",multiplication(num1,num2))
print("Division:",division(num1,num2))