x = {True: "yes", 1: "no", 1.0: "maybe"}
# print(x)
# output: {True: "maybe"}

xs = dict()
xs[True] = "yes"
xs[1] = "no"
xs[1.0] = "maybe"

print(xs)

print(True == 1 == 1.0) # This is why the dict ends up like that.

ys = dict()
ys[1] = "yes"
ys[True] = "no"

print(ys)
# As the keys keep being the same, the interpreter don't refresh them,
# it just keep using the first one.