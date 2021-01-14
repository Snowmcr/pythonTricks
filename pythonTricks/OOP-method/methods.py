class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"


obj = MyClass()
print(obj.method())
print(obj.classmethod()) # Just acces to the class, not the instance.
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
# print(MyClass.method())
# This would give an error because there's no instance.