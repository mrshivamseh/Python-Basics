with open("Profile.txt","r") as file:
    print(file.tell())

    print(file.readline())

    print(file.tell())

    file.seek(0)
    # print(file.seek(0))

    print(file.readline())

    print(file.readline())

