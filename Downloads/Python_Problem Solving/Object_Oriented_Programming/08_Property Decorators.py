# use a property decorator in the Car class to make the model attribute read-only
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model


myCar = Car("Toyota", "Corolla")
# myCar.model = "Camry"  # this will raise an AttributeError because model is read-only

print(myCar.get_brand())
print(myCar.model)
