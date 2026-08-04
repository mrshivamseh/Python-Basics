def student_info(**details):
    for key,value in details.items():
        print(key,":",value)


student_info(
    name="Shivam",
    age=20,
    course="Python"
)