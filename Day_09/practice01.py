def calculate_average(*numbers):
    total = sum(numbers)
    average  = total/len(numbers)

    return average

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

result = calculate_average(num1,num2,num3)

print("Average:",result)

