
students = []  # list to store all student dictionaries

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Add New Student ---")
        student = {}
        
        student["id"] = input("Student ID: ")
        student["name"] = input("Name: ")
        student["age"] = input("Age: ")
        student["birth"]= input("birth (yyyy-mm-dd :")
        student["grade"] = input("Grade (like A, B+, C): ")
        student["subjects"] = input("Subjects (comma separated): ")
        
        students.append(student)
        print("Student added successfully!\n")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo students found!\n")
        else:
            print("\n--- All Students ---")
            for s in students:
                print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")
                print(f"Grade: {s['grade']} | Subjects: {s['subjects']}")
                print("-" * 40)

    elif choice == "3":
        if len(students) == 0:
            print("\nNo students to update!\n")
        else:
            sid = input("Enter Student ID to update: ")
            found = False
            for s in students:
                if s["id"] == sid:
                    print("Found student! What do you want to change?")
                    print("1. Name   2. Age   3. Grade   4. Subjects")
                    field = input("Choose field (1-4): ")
                    
                    if field == "1":
                        s["name"] = input("New Name: ")
                    elif field == "2":
                        s["age"] = input("New Age: ")
                    elif field == "3":
                        s["grade"] = input("New Grade: ")
                    elif field == "4":
                        s["subjects"] = input("New Subjects (comma separated): ")
                    else:
                        print("Invalid choice!")
                    
                    print("Student updated successfully!")
                    found = True
                    break
            if not found:
                print("Student ID not found!")

    elif choice == "4":
        if len(students) == 0:
            print("\nNo students to delete!\n")
        else:
            sid = input("Enter Student ID to delete: ")
            for i in range(len(students)):
                if students[i]["id"] == sid:
                    students.pop(i)
                    print("Student deleted successfully!")
                    break
            else:
                print("Student ID not found!")

    elif choice == "5":
        print("\nThank you for using the Student Data Organizer!")
        print("Goodbye! Have a great day! ")
        break

    else:
        print("Invalid choice! Please enter number 1 to 5.")
