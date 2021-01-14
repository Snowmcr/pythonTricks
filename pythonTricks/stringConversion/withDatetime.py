class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"a {self.color} car, mileage: {self.mileage}"
    def __repr__(self):
        return f"a {self.color} car, bruh"


my_car = Car("red", 37281)

# Uses __repr__ magic method
print(repr(my_car))

# Uses __str__ magic method
print(my_car)
 """