def listComprehension():
    squares = [x * x for x in range(10)]
    print(squares)

    # structure:
    (values) = [(expression) for (value) in (collection)]

    # Turns to:

    (values) = []
    for (value) in (collection):
        (values).append((expression))


def comprehensionWithCondition():
    even_squares = [x * x for x in range(10) if x % 2 == 0]
    print(even_squares)

    # structure:
    [expression for value in collection if condition]


def differentWriting():
    even_squares = [x * x
                    for x in range(10)
                    if x % 2 == 0]
