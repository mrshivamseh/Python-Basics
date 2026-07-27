def greet(name="Shivam"):
    return "Hello,"+name

name = input("Enter your name:")

if name =="":
    result = greet()
else:
    result = greet(name)

print(result)
