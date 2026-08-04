from student import add_student, view_students,search_student,delete_student


while True:
    print("====Student Record System====")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        try:
            print("NEW CODE RUNNING")            name = input("Enter student name: ")
            age = int(input("Enter student age:"))

            add_student(name, age)
            print("Student added successfully!")

        except ValueError:
            print("Age must be a number. Please try again.")

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        search_student(name)

    elif choice == "4":
        name = input("Enter student name to delete: ")
        delete_student(name)

    elif choice == "5":
        print("Thank you for using the Student Record System.")
        break
    else:
        print("Invalid choice. Please try again.")

    

