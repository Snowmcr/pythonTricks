def dispatch_if(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x-y
    elif operator == "mul":
        return x*y
    elif operator == "div":
        return x/y


# dispatch_if("mul", 2, 8) 
# normally

def dispatch_dict(operator, x, y):
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,       
        "div": lambda: x / y        
    }.get(operator, lambda: None)()


h = dispatch_dict("add", 2, 5)
print(h)