# Case Study 1: Examination Result and Grace-Mark Validation

marks = []

# Read marks for five subjects
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))

    # Validate marks
    while mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        mark = int(input(f"Enter marks for subject {i}: "))

    # Apply grace marks if shortage is 5 or less
    if mark < 35 and 35 - mark <= 5:
        print("Grace marks applied to subject", i)
        mark = 35

    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 5

# Display results
print("\nFinal Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

# Check final result
if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")