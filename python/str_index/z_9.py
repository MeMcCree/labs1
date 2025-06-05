zdanie = input()

słowo = ''
for litera in zdanie:
    if litera != ' ':
        słowo += litera
    elif słowo:
        print(słowo)
        słowo = ''

if słowo:
    print(słowo)