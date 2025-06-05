pochlebce = {
    'Сладкоежка': {'банан', 'молоко', 'мороженое'},
    'Клубнично-банановый': {'клубника', 'молоко', 'банан', 'мороженое'},
    'Клубничный': {'клубника', 'молоко', 'мороженое'},
    'Хушаф': {'финики', 'молоко'},
    'Банановый': {'банан', 'молоко', 'финики'}
}

zapas = {}
for _ in range(5):
    towar, ilość = input().split(': ')
    zapas[towar] = int(ilość)

n = int(input())
zamówienia = [input() for i in range(n)]

for zamówienie in zamówienia:
    można_zrobić = True
    tymczasowy_zapas = zapas.copy()
    for składnik in pochlebce[zamówienie]:
        if tymczasowy_zapas.get(składnik, 0) == 0:
            można_zrobić = False
            break
        tymczasowy_zapas[składnik] -= 1
    
    if można_zrobić:
        zapas = tymczasowy_zapas
        print(f'Пожалуйста, ваш {zamówienie}. Приятного аппетита!')
    else:
        print('Извините, не можем выполнить заказ.')