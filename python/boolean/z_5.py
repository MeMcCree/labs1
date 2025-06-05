pojemność_wiadra = int(input())
grad_wykryty = False
obecna_pojemność = 0
sekundy = 0
wyjść = False

while True:
    pojemność_kropli = int(input())

    if not pojemność_kropli:
        break

    if pojemność_kropli > 20:
        grad_wykryty = True
    
    sekundy += 1
    obecna_pojemność += pojemność_kropli

    if obecna_pojemność >= pojemność_wiadra:
        print(f"Время заполнения {sekundy} секунд.")
        print("Града не было." if not grad_wykryty else "Град был!")
        wyjść = True
        break

if not wyjść:
    print("Ведро не полное.")

    if grad_wykryty:
        print("Град был!")
    else:
        print("Града не было.")