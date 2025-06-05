k = int(input())
b = int(input())

# y = kx + b

above = 0
below = 0
on = 0

s = input()
while s != 'END':
    x = int(s)
    y = int(input())

    ly = k * x + b

    if y > ly:
        above += 1
    elif y < ly:
        below += 1
    else:
        on += 1

    s = input()

if above:
    print(f'Выше прямой: {above}')

if below:
    print(f'Ниже прямой: {below}')

if on:
    print(f'На прямой: {on}')