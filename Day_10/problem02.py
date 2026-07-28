def student_info(**details):
    print("Student Information:")

    for key,value in details.items():
        print(key,":",value)


name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter your course:")

student_info(
    name=name,
    age=age,
    course=course
)