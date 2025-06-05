własna_częstość = int(input())
wymuszona_częstość = int(input())

cyfry = 0
temp = własna_częstość
while temp > 0:
    temp = temp // 10
    cyfry += 1

h = (10 ** (cyfry - 1))
pierwsza_cyfra = własna_częstość // h

if pierwsza_cyfra != 9:
    a = (pierwsza_cyfra + 1) * h
    a += własna_częstość % h
else:
    a = własna_częstość

b = własna_częstość // 10 * 10 + (własna_częstość % 10 - 1)
c = własna_częstość % 10 * h + własna_częstość // 10
d = własna_częstość % h * 10 + własna_częstość // h

if a == wymuszona_częstość:
    print("ДА 1")
elif b == wymuszona_częstość:
    print("ДА 2")
elif c == wymuszona_częstość:
    print("ДА 3")
elif d == wymuszona_częstość:
    print("ДА 4")
else:
    print("НЕТ")
