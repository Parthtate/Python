class Car:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Company Name: {self.brand}, Model: {self.model}"   
        # f"" called formatted string 



car_one = Car("Bugatti", "Divo")
print(car_one.fullName())
print(car_one.brand)