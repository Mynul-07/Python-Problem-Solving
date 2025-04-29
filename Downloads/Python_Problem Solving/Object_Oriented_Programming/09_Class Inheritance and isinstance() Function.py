# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "100kWH")
# print(my_tesla.model)
# print(my_tesla.full_name())
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
