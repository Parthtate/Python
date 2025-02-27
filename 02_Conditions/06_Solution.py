distance = int(input("Enter your travelled distance for Transportation mode: "))

if distance < 3:
    transportation_mode = "Walk"
elif distance < 14:
    transportation_mode = "Bike"
else:
    transportation_mode = "Car"

print("Your Transportation Mode is:", transportation_mode)            