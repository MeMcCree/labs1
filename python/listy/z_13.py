n = int(input())
m = int(input())

oryginały = set()
for i in range(n):
    oryginały.add(input())

zaszyfrowane = []
for i in range(m):
    zaszyfrowane.append(input())

rozszyfrowane = set()
wyniki = []

for wiadomość in zaszyfrowane:
    cyfry = ''.join(c for c in wiadomość if c.isdigit())
    k = int(cyfry) if cyfry else None
    if not k:
        continue

    rozszyfrowana = ''.join(wiadomość[i] for i in range(k - 1, len(wiadomość), k))
    if rozszyfrowana in oryginały and rozszyfrowana not in rozszyfrowane:
        wyniki.append(rozszyfrowana)
        rozszyfrowane.add(rozszyfrowana)

if wyniki:
    for linia in wyniki:
        print(linia)
else:
    print('NO')