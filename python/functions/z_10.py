def graph(func):
    print("x", end="")
    for x in range(-10, 1):
        print(f"\t{x}", end="")
    for x in range(1, 11):
        print(f"\t{x}", end="")
    print()

    print("y", end="")
    for x in range(-10, 11):
        y = eval(func, {'x': x})
        print(f"\t{y}", end="")
    print()