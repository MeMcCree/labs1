n = int(input())
suma_kwardratów = 0
kwadrat_sumy = 0

i = 1
while i <= n:
    suma_kwardratów += i ** 2
    kwadrat_sumy += i
    i += 1

kwadrat_sumy = kwadrat_sumy * kwadrat_sumy

print(kwadrat_sumy - suma_kwardratów)