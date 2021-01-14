def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    if value:
        return value
    else:
        return
        # The same


def foo3(value):
    if value:
        return value
        # The same


print(type(foo1(False)))
print(type(foo2(False)))
print(type(foo3(False)))
# They are all the same

print(type(foo1(True)))
