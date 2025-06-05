b = int(input())
c = int(input())
d = int(input())

a = c * b + d
conc = int(str(d) + str(c))

print(conc)
if (conc > a):
	print('ДА')
else:
	print('НЕТ')