from fractions import Fraction
s = input()

prefiks = ''
centyprefiks = 0
kiloprefiks = 0

for i in s:
    prefiks += i
    if prefiks == 'санти':
        centyprefiks += 1
        prefiks = ''
    elif prefiks == 'кило':
        kiloprefiks += 1
        prefiks = ''
    elif prefiks == 'метр':
        prefiks = ''

znaczenie = Fraction(1, 1)

for i in range(kiloprefiks):
    znaczenie *= 1000

for i in range(centyprefiks):
    znaczenie /= 100

znaczenie *= 100

if znaczenie.denominator != 1:
    print(f'1/{znaczenie.denominator}')
else:
    print(znaczenie.numerator)