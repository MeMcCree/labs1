n = int(input())
wyniki = {}

for i in range(n):
    imię, linia = input().split(': ')
    wyniki[imię] = wyniki.get(imię, 0) + int(linia)

for imię, lącznie in wyniki.items():
    if lącznie >= 75:
        print(imię)
