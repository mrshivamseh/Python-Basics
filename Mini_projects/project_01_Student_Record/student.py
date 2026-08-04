def add_student(name,age):
    with open("data.txt","r") as file:
        lines = file.readlines()

        #Duplicate check
    for line in lines:
        data = line.strip().split(",")

        if len(data) >= 3:
            if data[1].lower() == name.lower() and data[2] == str(age):
                print("Student already exists.")
                return
            

    student_id = len(lines) + 1  # Generate a unique ID based on the number of existing students

    with open("data.txt","a")as file:
        file.write(f"{name},{age}\n")


def view_students():
    with open("data.txt","r")as file:
        data = file.read()
        print(data)

def search_student(name):
    with open("data.txt","r")as file:
        found =False

        for line in file:
            if name.lower() in line.lower():
                print(line.strip())
                found = True


            if not found:
                print("Student not found.")


def delete_student(name):
    with open("data.txt","r")as file:
        lines = file.readlines()

    with open("data.txt","w")as file:
        found = False
        for line in lines:
            if name.lower() not in line.lower():
                file.write(line)
            else:
                found = True

        if found:
            print("Student deleted successfully.")
        else:
            print("Student not found.")



    