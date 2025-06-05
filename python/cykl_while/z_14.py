s = input()
prev_len = 1

i = 0
while True:
    prev_len = len(s)
    s = input()
    if len(s) < prev_len:
        break
    i += 1

if i % 2:
    print('Первый')
else:
    print('Второй')