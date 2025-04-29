# modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"


myCar = Car("Toyota", "Corolla")
print(myCar.get_brand())  # output: Toyota
