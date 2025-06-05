from collections import Counter

liczby = input().split()
wszystkie_liczby = ''.join(liczby)
ilość_liczb = Counter(wszystkie_liczby)
maksymalna_ilość = max(ilość_liczb.values())
najwięcej_wspólnych_liczb = [cyfra for cyfra, liczba in ilość_liczb.items() if liczba == maksymalna_ilość]

print(' '.join(sorted(najwięcej_wspólnych_liczb)))