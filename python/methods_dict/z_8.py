energii = list(map(float, input().split()))
interwały = {
    'до 10': [],
    'от 10 до 100': [],
    'от 100 до 1000': [],
    'свыше 1000': []
}

for e in energii:
    if e < 10:
        interwały['до 10'].append(e)
    elif 10 <= e < 100:
        interwały['от 10 до 100'].append(e)
    elif 100 <= e <= 1000:
        interwały['от 100 до 1000'].append(e)
    else:
        interwały['свыше 1000'].append(e)

for linia, znaczenia in interwały.items():
    if znaczenia:
        ilość = len(znaczenia)
        średnia = sum(znaczenia) / ilość
        print(f'{linia}: {ilość}, {średnia:.1f}')