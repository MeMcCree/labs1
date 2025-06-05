def main():
    liczba_tabel = int(input())
    ilość = 0

    while True:
        linia = input()

        if linia == "КОНЕЦ":
            break
        
        if "доска" in linia or "дощечка" in linia:
            ilość += 1
        
            print(f"Прибили {ilość} дощечку.")
        
            if ilość == liczba_tabel:
                print("ГОТОВО")
                return

    print("МАЛОВАТО")


main()