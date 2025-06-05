h = float(input())
m = float(input())
n = int(input())

ts = h * 60 + m
t = 12 * 60
t = t - ts

tp = t / n
if tp < 1:
    print('Не останавливаемся!')
else:
    print(f'{int(tp)} минут')