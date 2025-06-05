a = input()
b = input()
c = input()

if len(a) > len(b) or (len(a) == len(b) and a > b):
    a, b = b, a

if len(b) > len(c) or (len(b) == len(c) and b > c):
    b, c = c, b

if len(a) > len(c) or (len(a) == len(c) and a > c):
    a, c = c, a

if len(a) > len(b) or (len(a) == len(b) and a > b):
    a, b = b, a

if len(b) > len(c) or (len(b) == len(c) and b > c):
    b, c = c, b

if len(a) > len(c) or (len(a) == len(c) and a > c):
    a, c = c, a

print(a)
print(b)
print(c)