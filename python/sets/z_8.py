chore = set()
linia = input()
while linia:
    chore.add(int(linia))
    linia = input()

zaszczepione = set()
linia = input()
while linia:
    zaszczepione.add(int(linia))
    linia = input()

zwolnione = set()
linia = input()
while linia:
    zwolnione.add(int(linia))
    linia = input()

n = int(input())
zapytania = [int(input()) for _ in range(n)]

odpowiednie = chore | zaszczepione | zwolnione
wynik = [z for z in zapytania if z in odpowiednie]

if wynik:
    print(*set(wynik), sep='\n')