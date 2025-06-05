def main():
    linia = input()
    stos = []
    pary = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for litera in linia:
        if litera in pary:
            stos.append(litera)
        elif stos and pary.get(stos[-1]) == litera:
            stos.pop()
        else:
            print('NO')
            return
    
    print('YES' if len(stos) == 0 else 'NO')


if __name__ == "__main__":
    main()