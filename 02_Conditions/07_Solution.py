order_coffee = input("Order Coffee Size: \n Small, Medium, Large \n").lower()
extra_shot = True


if extra_shot:
    coffee = order_coffee + " with Extra Shot"
else:
    coffee = order_coffee

print("Your Coffee order is:", coffee)        
