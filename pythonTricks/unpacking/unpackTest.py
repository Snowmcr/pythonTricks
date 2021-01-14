def print_vector(x, y, z):
    print(f"<{x}, {y}, {z}>")


myList = [1, 2, 3]

print(myList[0])
print(*myList)

myDict = {"x": 1, "y": 2, "z": 3}

print(myDict)
print(*myDict)
print_vector(**myDict)
# It doesn't work if the arguments are no the same as the keys.
