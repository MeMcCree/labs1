numer = input()
dlina = int(input())

maksymalny_iloczyn = 0

for i in range(len(numer) - dlina + 1):
    iloczyn = 1
    podciąg = numer[i:i + dlina]
    
    for digit in podciąg:
        iloczyn *= int(digit)

    if iloczyn > maksymalny_iloczyn:
        maksymalny_iloczyn = iloczyn

print(maksymalny_iloczyn)