class Car:
    total_car = 0
    # whenever __init__() call, total_car increases by one

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullName(self):
        return f"{self.brand} {self.model}"    

    def fuel_type(self):
        return "Petrol or Disel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

Car("Tata", "Nexon")        
Car("Audi", "A7")
Car("Suzuki", "Alto")

ElectricCar("Tesla", "Tesla S", "85kWh")

print(Car.total_car)