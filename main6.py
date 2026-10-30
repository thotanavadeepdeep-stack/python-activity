# Case Study 4: Smart Parking Fee Management

vehicle = input("Enter vehicle type (bike/car): ").lower()

entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    # Convert entry time into minutes
    eh, em = map(int, entry.split(":"))
    xh, xm = map(int, exit_time.split(":"))

    start = eh * 60 + em
    end = xh * 60 + xm

    # Validate time
    if not (0 <= eh < 24 and 0 <= xh < 24 and
            0 <= em < 60 and 0 <= xm < 60):
        print("Invalid time.")

    elif end <= start:
        print("Exit time must be later than entry time.")

    elif vehicle not in ("bike", "car"):
        print("Invalid vehicle type.")

    else:
        # Calculate parking duration
        minutes = end - start

        # Charge every started hour
        hours = (minutes + 59) // 60

        # Calculate fee
        if vehicle == "bike":
            rate = 10
        else:
            rate = 20

        fee = hours * rate

        print("Parking duration:", minutes, "minutes")
        print("Billable hours:", hours)
        print("Total parking fee: Rs.", fee)

except ValueError:
    print("Invalid time format. Use HH:MM.")