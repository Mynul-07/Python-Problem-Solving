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

    def full_name(self):
        return f"{self.brand} {self.model} with a battery size of {self.battery_size}"


class Battery:
    def battery_info(self):
        return "This is a battery class"


class Engine:
    def engine_info(self):
        return "This is an engine class"


class ElectricCarTwo(Battery, Engine, ElectricCar, Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, battery_size)


my_tesla = ElectricCarTwo("Tesla", "Cyber truck", "100 kWH")
print(my_tesla.full_name())
print(my_tesla.battery_info())
print(my_tesla.engine_info())
