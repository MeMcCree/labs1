link = input().split('/')
wynik = [część.split('#')[0] for część in link if '#' in część]
print(wynik[0])