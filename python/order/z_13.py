a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

last_height = 0

if a > last_height:
    print('1 ', end='')
    last_height = a

if b > last_height:
    print('2 ', end='')
    last_height = b

if c > last_height:
    print('3 ', end='')
    last_height = c

if d > last_height:
    print('4 ', end='')
    last_height = d

if e > last_height:
    print('5 ', end='')
    last_height = e