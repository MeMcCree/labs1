ekwipunek = {}
linia = input()
while linia:
    ekwipunek[linia] = ekwipunek.get(linia, 0) + 1
    linia = input()

n = int(input())
for i in range(n):
    potrzebne = input()
    if ekwipunek.get(potrzebne, 0) > 0:
        print('Есть в наличии')
        ekwipunek[potrzebne] -= 1
    else:
        print('Нет в наличии')