mapa = [[0] * 10 for i in range(10)]
statek = '\u25A1'

for i in range(1, 11):
    kord = input().split()
    
    if 'к' in kord[0]:
        kord[0] = 'й' + kord[0][-1]
    
    if i <= 1:
        if kord[1] == 'в':
            for j in range(4):
                mapa[int(kord[0][1:]) - 1 + j][ord(kord[0][0]) - 1072] = statek
        else:
            for j in range(4):
                mapa[int(kord[0][1:]) - 1][ord(kord[0][0]) - 1072 + j] = statek
    
    if 2 <= i < 4:
        if kord[1] == 'в':
            for j in range(3):
                mapa[int(kord[0][1:]) - 1 + j][ord(kord[0][0]) - 1072] = statek
        else:
            for j in range(3):
                mapa[int(kord[0][1:]) - 1][ord(str(kord[0][0])) - 1072 + j] = statek
    
    if 4 <= i < 7:
        if kord[1] == 'в':
            for j in range(2):
                mapa[int(kord[0][1:]) - 1 + j][ord(kord[0][0]) - 1072] = statek
        else:
            for j in range(2):
                mapa[int(kord[0][1:]) - 1][ord(kord[0][0]) - 1072 + j] = statek
    else:
        mapa[int(kord[0][1:]) - 1][ord(kord[0][0]) - 1072] = statek

for i in range(10):
    for j in range(10):
        print(mapa[i][j], end=' ')
    print()