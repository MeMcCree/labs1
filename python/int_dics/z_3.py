elementy = {}
inp = input()
while inp != "":
    części = inp.split()
    element = części[0]
    częstliwości = set(map(float, części[1:]))
    elementy[element] = częstliwości
    inp = input()

zauważone = set()
inp = input()
while inp != "":
    zauważone.add(float(inp))
    inp = input()

wyniki = []
for element, czs in elementy.items():
    if czs.issubset(zauważone):
        wyniki.append(element)

for element in wyniki:
    print(element)