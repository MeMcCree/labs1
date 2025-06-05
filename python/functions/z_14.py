def square(trapezoids):
    total_area = 0.0
    for a, b, h in trapezoids:
        area = (a + b) * h / 2
        total_area += area
    print(total_area)