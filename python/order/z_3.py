x = float(input())

if (abs(x) < 1e-9):
	print('INFINITELY LARGE')
elif (abs(x) > 1e9):
	print('INFINITELY SMALL')
else:
	print(1 / x)