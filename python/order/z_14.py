s = input()
exp = s.split('e')
if len(exp) > 1:
    s = float(exp[0]) * 10 ** int(exp[1])
else:
    num = s.split('_')
    s = float(''.join(num))

v = input()
exp = v.split('e')
if len(exp) > 1:
    v = float(exp[0]) * 10 ** int(exp[1])
else:
    num = v.split('_')
    v = float(''.join(num))

t = s / v / 60 / 60 / 24 / 365
print(t)