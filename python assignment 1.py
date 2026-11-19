students = {
    101: ("Aarav", "Computer", 88),
    102: ("Isha", "Electronics", 76),
    103: ("Rohan", "Mechanical", 65)
}

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. Display all students")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))
        if roll in students:
            print("Roll number already exists!")
        else:
            name = input("Enter name: ")
            branch = input("Enter branch: ")
            marks = int(input("Enter marks: "))
            students[roll] = (name, branch, marks)   
            print("Student added.")

    elif choice == "2":
        roll = int(input("Enter roll number to delete: "))
        if roll in students:
            del students[roll]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "3":
        roll = int(input("Enter roll number to update: "))
        if roll in students:

            old = students[roll]
            print("Current details:", old)
            name = input("Enter new name: ")
            branch = input("Enter new branch: ")
            marks = int(input("Enter new marks: "))
            students[roll] = (name, branch, marks)
            print("Student updated.")
        else:
            print("Student not found.")

    elif choice == "4":
        rolls = list(students.keys())      
        rolls.sort()
        print("\nRoll No\tName\tBranch\t\tMarks")
        for r in rolls:
            print(r, "\t", students[r][0], "\t", students[r][1], "\t", students[r][2])

    elif choice == "5":
        print("Final student records:")
        for r in students:
            print(r, students[r])
        break

    else:
        print("Invalid choice, try again.")
