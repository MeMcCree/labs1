n = int(input())
m = int(input())

macierz = []
for i in range(n):
    rząd = []
    for j in range(m):
        rząd.append(input())
    macierz.append(rząd)

wynik = []
for i in range(n):
    for j in range(m):
        imię = macierz[i][j]
        dlina_imienia = len(imię)
        pierwsza_litera = imię[0]
        naruszenia = []
        
        if i > 0:
            dogóry = macierz[i - 1][j]
            if len(dogóry) == dlina_imienia or dogóry[0] == pierwsza_litera:
                naruszenia.append((i, j))
        if i < n - 1:
            nadół = macierz[i + 1][j]
            if len(nadół) == dlina_imienia or nadół[0] == pierwsza_litera:
                naruszenia.append((i, j))
        
        lewo_dobrze = prawo_dobrze = False
        
        if j > 0:
            nalewo = macierz[i][j - 1]
            if len(nalewo) == dlina_imienia or nalewo[0] == pierwsza_litera:
                nalewo_dobrze = True
        
        if j < m - 1:
            naprawo = macierz[i][j + 1]
            if len(naprawo) == dlina_imienia or naprawo[0] == pierwsza_litera:
                prawo_dobrze = True

        if j == 0:
            if not prawo_dobrze:
                naruszenia.append((i, j))
        elif j == m - 1:
            if not nalewo_dobrze:
                naruszenia.append((i, j))
        else:
            if not nalewo_dobrze or not prawo_dobrze:
                naruszenia.append((i, j))

        wynik.extend(naruszenia)

wynik = sorted(set(wynik))
for koordynata in wynik:
    print(koordynata)