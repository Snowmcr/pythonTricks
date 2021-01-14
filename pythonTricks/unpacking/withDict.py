def print_vector(x, y, z):
    print(f"<{x}, {y}, {z}>")


dict_vec = {"x": 1, "y": 0, "z": 1}

print_vector(**dict_vec)
