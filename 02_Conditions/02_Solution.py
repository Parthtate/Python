age = int(input("Please enter your age: "))
day = "Wednesday"

ticket_price = 0

# price = 12 if age >= 18 else 8 

if (age >= 18):
    ticket_price = 12
elif (age < 9):
    ticket_price = 8   

if (day == "Wednesday"):
    ticket_price -= 2

print("Your Ticket price is: $",ticket_price)    
