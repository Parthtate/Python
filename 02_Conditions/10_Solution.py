species = input("Enter Your Pet Species:  DOG or CAT \n").lower()
age = int(input("Enter pet age: "))

if age < 2:
    food = "Puppy Food"
elif age < 5:
    food = "Senior Cat or Dog Food"
elif age >= 18:
    print("Invalid age")  
    exit() 
else: 
    food = "Senior cat or food dog"    

print("Based on age your pet food is:", food)
