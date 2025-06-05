las = []
linia = input()
while linia:
    las.append([int(x) for x in linia.split(" : ")])
    linia = input()

krytyczny = int(input())
for rząd in las:
    print("\t".join("0" if x < krytyczny else str(x) for x in rząd))