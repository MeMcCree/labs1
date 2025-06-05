głębokość_ryb = {}
linia = input()
while linia:
    ryba, głębokość = linia.split()
    głębokość = int(głębokość)
    if ryba in głębokość_ryb:
        minimalna_głębokość, maksymalna_głębokość = głębokość_ryb[ryba]
        głębokość_ryb[ryba] = (min(minimalna_głębokość, głębokość), max(maksymalna_głębokość, głębokość))
    else:
        głębokość_ryb[ryba] = (głębokość, głębokość)
    linia = input()

print(głębokość_ryb)