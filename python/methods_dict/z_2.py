n = int(input())

zapas = {}
for i in range(n):
    imię, ilość = input().split()
    zapas[imię] = int(ilość)

konsumpcja = {}
for i in range(n):
    imię, tempo = input().split()
    konsumpcja[imię] = int(tempo)

dni = min(zapas[imię] // konsumpcja[imię] for imię in zapas)
print(dni)