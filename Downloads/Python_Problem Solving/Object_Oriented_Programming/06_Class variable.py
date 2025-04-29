# add a class variable to Car that keeps tack of the number of cars created
class Car:
    car_count = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.car_count += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return F"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "100kWH")
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

Car1 = Car("Toyota", "Corolla")
Car2 = Car("Honda", "Civic")
print(Car.car_count)
