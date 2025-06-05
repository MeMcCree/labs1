a = int(input())
k = int(input())

obecne = a
for t in range(1, k):
    eks = obecne
    if eks == 0:
        bit = "0"
    else:
        bity = []
        while eks > 0:
            bity.append(str(eks % 2))
            eks //= 2
        bit = "".join(reversed(bity))

    jedynki = 0
    for cyfra in bit:
        if cyfra == "1":
            jedynki += 1

    igrek = jedynki
    if igrek == 0:
        nowe = "0"
    else:
        nowebity = []
        while igrek > 0:
            nowebity.append(str(igrek % 2))
            igrek //= 2
        nowe = "".join(reversed(nowebity))
    powiązanie = bit + nowe
    znaczenie = 0
    for cyfra in powiązanie:
        if cyfra == "1":
            znaczenie = znaczenie * 2 + 1
        else:
            znaczenie = znaczenie * 2
    obecne = znaczenie

print(obecne)