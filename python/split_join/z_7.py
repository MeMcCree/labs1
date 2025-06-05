separator, n, linia = input().split(' ', 2)
n = int(n)
słowa = linia.split(separator)

przefiltrowane = [słowo for słowo in słowa if len(set(słowo)) >= n]

print(separator[::-1].join(przefiltrowane))