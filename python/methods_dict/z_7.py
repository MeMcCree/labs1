linia = input()
ilości = {litera: 0 for litera in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for litera in linia:
    if litera.isalpha():
        ilości[litera.upper()] += 1
print(ilości)