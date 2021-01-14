class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color}, {self.mileage})"
        # self.__class__.__name__ is for the name of the class we are in.


my_car = Car("green", 1209)

print(my_car)

# Since there's no __str__, it just uses __repr__ method.
# Very good to at least add a __repr__ method to the classes.
