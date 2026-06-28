def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                roll = input("Enter Roll No: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({roll: {"Name": name, "Age": age, "City": city}})
                print("Student Added Successfully.")

            elif choice == "2":
                roll = input("Enter Roll No: ")
                print(students.get(roll, "Student Not Found"))

            elif choice == "3":
                for roll, data in students.items():
                    print(roll, ":", data)

            elif choice == "4":
                print("Exiting...")
                break

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Invalid Input.")

student_database()
