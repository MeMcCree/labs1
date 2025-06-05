linia = input()
dlina = len(linia)

pierwsza_część = ''
druga_część = ''

środek = (dlina + 1) // 2
for i in range(środek):
    pierwsza_część += linia[i]

for i in range(środek, dlina):
    druga_część += linia[i]

wynik = ''

for i in range(środek):
    wynik += pierwsza_część[i]
    
    if i < len(druga_część):
        wynik += druga_część[i]

print(wynik)