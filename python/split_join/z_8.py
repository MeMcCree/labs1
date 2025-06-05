słowa = input().split(", ")
wynik = ["flower" if i % 2 == 0 else "gemstone" for i in range(len(słowa))]
print("; ".join(wynik))