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


class Battery:
    def battery_info(self):
        return "My Battery charging is necessary to run a tesla car"

class Engine:
    def engine_info(self):
        return "Engine wants to fuel to run the car on road"

class ElectricCar(Car, Battery, Engine):
    pass

car_one = ElectricCar("Tesla", "Model S")
print(car_one.battery_info())
print(car_one.engine_info())