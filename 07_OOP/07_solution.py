class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"    

    def fuel_type(self):
        return "Petrol or Disel"

    @staticmethod
    def general_description():
        return "Car used for tranportation or traveling, etc"

car_one = Car("Tata", "Nexon")

print(car_one.general_description()) 
# for this method required self keyword, but first call @staticmethod then only it works!

# print(Car.general_description())
# for this method does not required self keyword

# staticmethod is access for only class, not for object
# that's why we abel to use Car.general_description(), but not car_one.general_description(), cause it is an object