n = int(input())
m = int(input())
k = int(input())

długość_łącznie = 120 * k

najlepsza_para = (0, 0)
najlepsza_suma = -1
maksymalny_igrek = długość_łącznie // m
for igrek in range(1, maksymalny_igrek + 1):
    ostatek = długość_łącznie - igrek * m
    
    if ostatek % n != 0:
        continue
    
    if ostatek <= 0:
        continue

    eks = ostatek // n
    
    if eks < 1:
        continue
    
    suma = 5 * igrek + 2 * eks
    if suma > najlepsza_suma:
        najlepsza_suma = suma
        najlepsza_para = (eks, igrek)

print(najlepsza_suma)
print(najlepsza_para)