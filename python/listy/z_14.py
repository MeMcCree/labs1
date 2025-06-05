m = int(input())
n = int(input())

znaczenia = []
for i in range(n):
    znaczenia.append(int(input()))

najlepsza_para = (0, 0)
maksymalny_iloczyn = 0

moduły = {}
for u in znaczenia:
    moduł = u % m
    komplement = (m - moduł) % m
    
    if komplement in moduły:
        t = moduły[komplement]
        iloczyn = u * t
    
        if iloczyn > maksymalny_iloczyn:
            maksymalny_iloczyn = iloczyn
            najlepsza_para = (u, t)

    if u > moduły[moduł] or moduł not in moduły:
        moduły[moduł] = u

print(*najlepsza_para)