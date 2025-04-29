# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"


my_tesla = ElectricCar("Tesla", "Model S", "100kWH")
# print(my_tesla.model)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
