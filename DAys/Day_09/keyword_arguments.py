def student_info(name,age,course):
    return f"Name: {name},Age:{age},Course:{course}"

name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter your course:")

result = student_info(
    name=name,
    age=age,
    course=course
)

print(result)