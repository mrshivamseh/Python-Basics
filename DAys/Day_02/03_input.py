name = input("Enter your name: ")  #string
age = int(input("Enter your age: "))  #integer
weight = float(input("Enter your weight: "))  #float
height = float(input("Enter your height: "))  #float
is_student = input("Are you a student? (yes/no): ").lower() == "yes"  #boolean

print("Name:", name)
print("Age:", age)
print("Weight:", weight)
print("Height:", height)
print("Is Student:", is_student)