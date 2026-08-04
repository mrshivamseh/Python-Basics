DAY 09 – FUNCTIONS (PART 2)

1. Default Parameter
def greet(name="Shivam"):
    return "Hello, " + name

2. Keyword Argument
student_info(name="Shivam", age=20)

3. *args
- Multiple positional arguments receive karta hai.
- Tuple ke form me milta hai.

def add(*numbers):
    return sum(numbers)

4. **kwargs
- Multiple keyword arguments receive karta hai.
- Dictionary ke form me milta hai.

def info(**details):
    for key, value in details.items():
        print(key, value)

5. *args + **kwargs
def function(*args, **kwargs):
    pass

*args → positional arguments
**kwargs → keyword arguments

6. Important:
input() → string deta hai
Number ke liye:
int(input("Enter number: "))