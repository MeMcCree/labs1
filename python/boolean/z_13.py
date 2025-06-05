szerokość_pola = int(input())
liczba_słów = int(input())

offset = 0
krok = 1
do_prawej = True
while liczba_słów > 0:
    słowo = input()
    słowo_ze_spacjami = ' ' * offset + słowo
    długość_linii = len(słowo_ze_spacjami)

    if do_prawej:
        if długość_linii == szerokość_pola:
            do_prawej = False
            print(słowo_ze_spacjami)
        elif długość_linii > szerokość_pola:
            do_prawej = False
            offset = szerokość_pola - len(słowo)
            print(' ' * offset + słowo)
        else:
            print(słowo_ze_spacjami)
            offset += 1
    else:
        offset = szerokość_pola - len(słowo) - krok
        słowo_ze_spacjami = ' ' * offset + słowo

        if len(słowo_ze_spacjami) == szerokość_pola:
            do_prawej = True
            offset = 1
            krok = 1
            print(słowo_ze_spacjami)
        elif len(słowo_ze_spacjami) > szerokość_pola:
            do_prawej = True
            offset = 1
            krok = 1
            print(słowo)
        else:
            print(słowo_ze_spacjami)
            krok += 1
        
        if offset <= 0:
            do_prawej = True
            offset = 1
            krok = 1

    liczba_słów -= 1