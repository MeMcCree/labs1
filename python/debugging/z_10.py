s = input()

last = ''
while len(s):
    if 100 >= len(s) <= 999:
        print(last)
    elif len(s) % 2 == 0:
        print(s + s)
    elif len(s) % 3 == 0:
        print(s + s + s)
    else:
        print(s)

    last = s
    s = input()