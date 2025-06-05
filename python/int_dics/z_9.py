plan = {}
linia = input()
while linia:    
    bus, czas = linia.split()
    godziny, minuty = map(int, czas.split(':'))
    plan[bus] = plan.get(bus, []) + [godziny * 60 + minuty]
    linia = input()

godziny, minuty = map(int, input().split(':'))
obecny_czas = godziny * 60 + minuty
potrzebne_busy = set(input().split())
buforowy_czas = 6

minimalne_czekanie = float('inf')
for bus in potrzebne_busy:
    if bus in plan:
        for czas_busa in plan[bus]:
            if czas_busa >= obecny_czas + buforowy_czas:
                czekanie = czas_busa - obecny_czas - buforowy_czas
                minimalne_czekanie = min(minimalne_czekanie, czekanie)

print(minimalne_czekanie if minimalne_czekanie != float('inf') else None)