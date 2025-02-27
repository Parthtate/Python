user_password = input("Enter Your password: ")
password_length = len(user_password)

if password_length <= 6:
    strength = "Weak"
elif password_length < 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password strength is:", strength)         
    