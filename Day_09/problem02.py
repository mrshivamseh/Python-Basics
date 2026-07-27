def student_info(**details):
    print("Student information:")

    for key,value in details.items():
        print(key,":",value)


name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter you course:")

student_info(
    name=name,
    age=age,
    course=course
)