while True:
    number = int(input("Enter number b/w 1 to 10: "))

    # if number <= 10 and number >= 1:
    if 1 <= number <= 10:
        print("Thanks")
        break
    else: 
        print("Invalid number, please try again")