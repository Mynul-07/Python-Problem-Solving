class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


Car1 = Car("Toyota", "Corolla")
print(Car1.model)  # Output: Corolla


Car2 = Car("Honda", "Civic")
print(Car2.brand)  # Output: Honda
print(Car2.model)  # Output: Civic
