linia = input()
słowa = linia.split()
lista_liter = []
lista_nieliter = []

for słowo in słowa:
    nielitery = ''.join(litera for litera in słowo if not litera.isalpha())
    litery = ''.join(litera for litera in słowo if litera.isalpha())

    if litery:
        lista_liter.append(litery.capitalize())
    
    if nielitery:
        lista_nieliter.append(nielitery)

if lista_liter:
    print(' '.join(lista_liter))
if lista_nieliter:
    print(' '.join(lista_nieliter))