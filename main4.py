# Case Study 2: Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))

# Validate attendance data
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance data.")

else:
    # Calculate current attendance percentage
    percentage = (attended / total) * 100

    print("Current attendance:", round(percentage, 2), "%")

    # Calculate classes needed to reach 75%
    future = 0

    while ((attended + future) / (total + future)) * 100 < 75:
        future += 1

    if future == 0:
        print("You already meet the 75% attendance requirement.")
    else:
        print("Consecutive classes to attend:", future)