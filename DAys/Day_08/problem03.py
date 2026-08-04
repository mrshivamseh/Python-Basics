def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"

    else:
        return "Fail"

marks = int(input("Enter your marks:"))

grade = calculate_grade(marks)

print("Grade:",grade)

       
