
""" 
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients})"


my_object = Pizza(["cheese", "tomatoes"])
my_object2 = Pizza(["cheese", "tomatoes", "ham"])
my_object3 = Pizza(["cheese", "tomatoes", "ham", "mushrooms"])
# Too hard 
"""

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients})"

    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["cheese", "tomatoes", "ham", "mushrooms"])

my_pizza = Pizza.margherita()
print(my_pizza)
my_pizza2 = Pizza.prosciutto()
print(my_pizza2)