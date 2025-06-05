s = input()

sm = 0
n = 0
while len(s):
    sm += s == 'да'
    n += 1

    s = input()

if n != 0 and sm / n >= 0.8:
    print('Достигли')
else:
    print('Пока нет')
