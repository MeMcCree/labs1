słowo = input()
while słowo:
    if len(set(słowo)) == len(słowo):
        print(słowo)
    słowo = input()