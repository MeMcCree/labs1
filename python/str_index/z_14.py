słowo = input()

dlina = len(słowo)
if dlina % 2 == 1:
    środek = dlina // 2
    start, koniec = środek, środek
else:
    środek = dlina // 2
    start, koniec = środek - 1, środek

for i in range(środek + 1):
    rząd = [' '] * dlina
    
    if start >= 0:
        rząd[start] = słowo[start]
    if koniec < dlina:
        rząd[koniec] = słowo[koniec]
    
    print(''.join(rząd))
    
    koniec += 1
    start -= 1