n = int(input())
zdażenia = {}
for i in range(n):
    dzień, miesiąc, zdażenie = input().split(maxsplit=2)
    zdażenia.setdefault(miesiąc, []).append((int(dzień), zdażenie))

nazwa = input()
dzień, zdażenie = min(zdażenia[nazwa], key=lambda x: x[0])
print(zdażenie)