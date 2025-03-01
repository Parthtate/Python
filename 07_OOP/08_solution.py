class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    @property
    def brand(self):
        return self.__brand   

    def fullName(self):
        return f"{self.__brand} {self.model}"


my_car = Car("Buggati", "Model S")
my_car.brand = "tata"
print(my_car.brand)

