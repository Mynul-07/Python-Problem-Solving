# Add a static method to the Car class that returns a general description of a car
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation"


myCar = Car("Tata", "Safari")
print(myCar.general_description())
