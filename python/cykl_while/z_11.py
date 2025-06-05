dx = 0
dy = 1

x = 0
y = 0

s = input()

while s != 'СТОП':
    match s:
        case 'шаг':
            x += dx
            y += dy
        case 'направо':
            dx, dy = dy, -dx
        case 'налево':
            dx, dy = -dy, dx

    s = input()

print(x, y)