def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    else:
        return "Invalid operaton"

num1 = int(input("Enter first number:")) 
num2 = int(input("Enter secound number:"))
operation = input("Enter operation(+,-,*,/):")

result = calculator(num1,num2,operation)

print("Result:",result)

                    
