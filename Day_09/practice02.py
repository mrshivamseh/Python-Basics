def student_profile(**details):
    print("Student Profile:")

    for key,value in details.items():
        print(key,":",value)



name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter you course:")
city = input("Enter you city:")

student_profile(
    name = name,
    age = age,
    course = course,
    city = city
)
