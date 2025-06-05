x = int(input())

if x == 0:
    print(50)
elif x <= 30:
    print(int(x * 1.5))
elif 30 < x <= 70:
    print(int(x * 1.1))
else:
    print(x)