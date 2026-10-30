# Case Study 6: Password Policy Validation

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isalnum():
        has_special = True

if (len(password) >= 8 and has_upper and has_lower
        and has_digit and has_special):
    print("Strong password")
else:
    print("Weak password")

    print("Password must contain:")
    print("- At least 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One digit")
    print("- One special character")