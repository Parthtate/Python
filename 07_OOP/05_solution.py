class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

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

safari = Car("Tata", "Safari")  
tesla = ElectricCar("Tesla", "Tesla S", "85kWh")

print(safari.fullName())
print(safari.fuel_type())

print(tesla.fullName())
print(tesla.fuel_type())
    
# polymorphism is same method but different behaviour 
# fuel_type method is same method but act differ for respective class    