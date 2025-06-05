numer = input()
dlina = len(numer)
wyniki = [numer[i:dlina - i] for i in range((dlina + 1) // 2)]
print(*wyniki, sep='\n')