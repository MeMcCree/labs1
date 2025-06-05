czajnik = int(input())
kubek = int(input())
liczba = int(input())

for i in range(1, liczba + 1):
    if czajnik >= kubek:
        czajnik -= kubek
        print('Чашечка', i, 'полная. В чайнике осталось', czajnik, end='.\n')
    elif czajnik > 0:
        print('Чашечка', i, 'неполная. В чайнике осталось', 0, end='.\n')
        czajnik = 0
    else:
        print('Чашечка', i, 'пустая. В чайнике осталось', czajnik, end='.\n')