def main():
    części = {"хобот": 0, "хвост": 0, "нога": 0, "ухо": 0, "глаз": 0, "рот": 0}
    while True:
        try:
            nazwa = input()
        except Exception as e:
            break
        
        if nazwa == "ОБЕД":
            break

        część = input()
        if część in części:
            części[część] += int(nazwa)
            
            słonie = min(
                części["хобот"],
                części["хвост"],
                części["рот"],
                części["ухо"] // 2,
                części["глаз"] // 2,
                części["нога"] // 4
            )

            if słonie > 0:
                print("Есть слон!")
                print(słonie)
                return

    słonie = min(
        części["хобот"],
        części["хвост"],
        części["рот"],
        części["ухо"] // 2,
        części["глаз"] // 2,
        części["нога"] // 4
    )

    if słonie > 0:
        print("Есть слон!")
        print(słonie)
    else:
        print("Какие-то слоны нецелые. Пошли обедать.")


main()