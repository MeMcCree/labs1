vol = input()

# mods: 4 12 20

frs = 0
if (vol == 'пенс'):
	frs = 4 * int(input())
else:
	frs = int(input())

afs = frs // 960
frs -= afs * 960

ash = frs // 48
frs -= ash * 48

aps = frs // 4
frs -= aps * 4

if (afs != 0):
	print('Фунтов:', afs)

if (ash != 0):
	print('Шиллингов:', ash)

if (aps != 0):
	print('Пенсов:', aps)

if (frs):
	print('Фартингов:', frs)