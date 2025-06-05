n = int(input())

dzieci = []
for i in range(n):
    dzieci.append(input())

m = int(input())

dostali_prezent = set()
for i in range(m):
    imię = input()
    
    if imię not in dostali_prezent:
        print(f"Вот твой подарок, {imię}!")
        dostali_prezent.add(imię)
    else:
        print(f"{imię}, всем по одному подарку!")
