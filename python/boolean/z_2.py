znaleziono = False

linia = input()
while linia != 'ВСЁ':
    if 'Звезд' in linia or 'звезд' in linia:
        znaleziono = True
    linia = input()

if not znaleziono:
    print('НЕТ')
else:
    print('Загадывай!')