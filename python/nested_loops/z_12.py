n = int(input())
prędkość = 0
ostatnia_prędskość = 0
ma_nadprędkość = False
cała_nadprędkość = True

for i in range(n):
    miara = int(input())
    nadprędkość = False
    
    for i in range(miara):
        speed = int(input())

        if speed > 60:
            ma_nadprędkość = True
            nadprędkość = True
        elif speed > prędkość and not nadprędkość:
            prędkość = speed

    if nadprędkość:
        prędkość = ostatnia_prędskość
    else:
        ostatnia_prędskość = prędkość
        cała_nadprędkość = False

if cała_nadprędkość:
    print(0)
else:
    print(prędkość)

if ma_nadprędkość:
    print("ДА")
else:
    print("НЕТ")