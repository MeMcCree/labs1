linii = []
linia = input()
while linia != '':
    linii.append(linia)
    linia = input()

start = -1
koniec = -1
for i in range(len(linii)):
    if "Все хорошо" in linii[i]:
        if start == -1:
            start = i
        else:
            end = i

for i in range(end - 1, start, -1):
    print(linii[i])