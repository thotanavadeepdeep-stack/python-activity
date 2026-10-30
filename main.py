name = input("Enter student name: ")

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
    


