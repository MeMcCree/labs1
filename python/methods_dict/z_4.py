d = {}
linia = input()
while linia:
    k, v = linia.split(': ', 1)
    d[v] = k
    linia = input()

n = int(input())
for i in range(n):
    x = input()
    print(d[x])