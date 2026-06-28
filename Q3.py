def manage_marks():
    marks = []

    try:
        for i in range(5):
            mark = float(input(f"Enter marks of subject {i+1}: "))
            marks.append(mark)

        average = sum(marks) / len(marks)

        print("Marks:", marks)
        print("Average:", average)
        print("Highest:", max(marks))
        print("Lowest:", min(marks))

        marks.sort(reverse=True)
        print("Descending Order:", marks)

    except ValueError:
        print("Error: Please enter numeric values only.")

manage_marks()
