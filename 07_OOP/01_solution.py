class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tata", "Safari")        
car2 = Car("Honda", "city")

print(car1.brand)
print(car2.brand)

# creating attribute or object means variable
# 'car1, car2' object is not callable 
# __init__ is constructor
# self keyword same as this in JS


