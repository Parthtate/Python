class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    # Only access my Car Class, not for other is known as Encapsulation
    # getter method
    def get_brand(self):
        return self.__brand    


    def fullName(self):
        return f"{self.__brand} {self.model}"




car_one = Car("Tata", "Nano")
# print(car_one.model)            
print(car_one.get_brand())            
# print(car_one.__brand)            
# print(car_one.fullName())            