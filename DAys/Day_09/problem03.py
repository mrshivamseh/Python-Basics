def student_result(*numbers,**details):
    total = sum(numbers)

    print("Student information:")

    for key,value in details.items():
        print(key,":",value)


    print("Total marks:",total)


num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

name = input("Enter your name:")
course = input("Enter your course:")

student_result(
    num1,
    num2,
    num3,
    name=name,
    course=course
)