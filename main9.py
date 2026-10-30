# Case Study 8: Food Waste Monitoring System

days = int(input("Enter number of days: "))

if days <= 0:
    print("Please enter a positive number of days.")
else:
    waste_list = []

    # Input food waste for each day
    for i in range(days):
        waste = float(input("Enter food waste in kg for day "
                            + str(i + 1) + ": "))

        if waste < 0:
            print("Invalid waste value.")
            break

        waste_list.append(waste)

    else:
        total_waste = sum(waste_list)
        average_waste = total_waste / days

        print("\nFood Waste Report")
        print("Daily waste:", waste_list)
        print("Total food waste:", total_waste, "kg")
        print("Average daily waste:", round(average_waste, 2), "kg")

        if average_waste > 5:
            print("Status: High food waste")
        else:
            print("Status: Low food waste")