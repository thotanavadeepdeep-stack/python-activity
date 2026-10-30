# Case Study 10: Student Academic Risk Classification

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Please enter a valid number of subjects.")
else:
    marks = []
    valid = True

    for i in range(n):
        mark = float(input("Enter marks for subject "
                           + str(i + 1) + ": "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            valid = False
            break

        marks.append(mark)

    if valid:
        average = sum(marks) / n

        print("\nStudent Name:", name)
        print("Marks:", marks)
        print("Average Marks:", round(average, 2))

        if average < 40:
            print("Academic Risk: High")
        elif average < 60:
            print("Academic Risk: Medium")
        else:
            print("Academic Risk: Low")