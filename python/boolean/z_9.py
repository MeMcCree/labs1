def main():
    odległosci = []

    d = int(input())

    while d >= 0:
        odległosci.append(d)
        d = int(input())

    if odległosci[0] < 35:
        print("ALARM")
        return

    wynik = []

    liczba = 1
    znak = 0
    for i in range(1, len(odległosci)):
        if odległosci[i] < 35:
            for r in wynik:
                print(r)
            print("ALARM")
            return

        if odległosci[i] == odległosci[i - 1]:
            continue
        
        if znak == 0:
            znak = 1 if odległosci[i] > odległosci[i - 1] else -1
            liczba += 1
        elif znak == 1 and odległosci[i] < odległosci[i - 1]:
            wynik.append(liczba)
            liczba = 2
            znak = -1
        elif znak == -1 and odległosci[i] > odległosci[i - 1]:
            wynik.append(liczba)
            liczba = 2
            znak = 1
        else:
            liczba += 1

    if liczba > 1:
        wynik.append(liczba)

    for x in wynik:
        print(x)


main()