marks = float(input("Enter your marks: "))
if marks >= 90:
    print("You have passed the exam.", "Grade A")
elif marks >= 80:
    print("You have passed the exam.", "Grade B")
elif marks >= 70:
    print("You have passed the exam.", "Grade C")
elif marks >= 60:
    print("You have passed the exam.", "Grade D")
else:
    print("You have failed the exam.", "Grade F")
