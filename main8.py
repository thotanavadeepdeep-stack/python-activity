# Case Study 7: Student Marks Matrix Analysis

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Enter positive numbers for students and subjects.")
else:
    marks = []

    # Read marks of each student
    for i in range(students):
        row = []
        print("Enter marks for Student", i + 1)

        for j in range(subjects):
            mark = float(input("Subject " + str(j + 1) + ": "))
            row.append(mark)

        marks.append(row)

    # Calculate total and average
    print("\nStudent Marks Analysis")

    for i in range(students):
        total = sum(marks[i])
        average = total / subjects

        print("Student", i + 1)
        print("Marks:", marks[i])
        print("Total:", total)
        print("Average:", round(average, 2))