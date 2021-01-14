if cond = "cond_a":
    handle_a()
elif cond == "cond_b":
    handle_b()
else:
    handle_default()

def func(a, b):
    return a + b

funcs = [my func]
funcs[0](2, 3)
# It would return 5.