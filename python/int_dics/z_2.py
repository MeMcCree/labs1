ptaki = {}
inp = input()
while inp != "":
    name, count = inp.split(": ")
    ptaki[name] = ptaki.get(name, 0) + int(count)
    inp = input()

print(ptaki)