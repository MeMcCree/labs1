obój = set()
flet = set()
saksofon = set()

imię = input()
while imię != '':
    obój.add(imię)
    imię = input()

imię = input()
while imię != '':
    flet.add(imię)
    imię = input()

imię = input()
while imię != '':
    obój.add(imię)
    imię = input()

tylko_na_jednym = (obój - flet - saksofon) | (flet - obój - saksofon) | (saksofon - obój - flet)
for muzyk in tylko_na_jednym:
    print(muzyk)
