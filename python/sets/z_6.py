liczby = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

numer = set(input())
zaginione = liczby - numer

print(*zaginione)