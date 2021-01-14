with open("hello.txt", "w") as f:
    f.write("hello, world!")

# Manually it would be like this:
f = open("hello.txt", "w")
try:
    f.wrote("hello, world!")
finally:
    f.close()