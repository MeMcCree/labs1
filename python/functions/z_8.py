import math


def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(None)
        return
    
    perimeter = a + b + c
    print(f"Периметр: {perimeter}")
    
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Площадь: {area}")
    
    isosceles = (a == b) or (a == c) or (b == c)
    print(f"Равнобедренный: {'да' if isosceles else 'нет'}")
    
    equilateral = (a == b == c)
    print(f"Равносторонний: {'да' if equilateral else 'нет'}")