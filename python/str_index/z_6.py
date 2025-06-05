numer = input()
maksymalny_iloczyn = 0

for i in range(len(numer) - 4):
    iloczyn = 1
    
    for j in range(5):
        iloczyn *= int(numer[i + j])

    maksymalny_iloczyn = max(maksymalny_iloczyn, iloczyn)

print(maksymalny_iloczyn)