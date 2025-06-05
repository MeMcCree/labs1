pr = ""

while True:
    s = input()
    
    if len(s) == 0:
        break
    
    ln = len(s)
    if 100 <= ln <= 999:
        print(pr)
    elif ln % 2 == 0:
        print(s * 2)
    elif ln % 3 == 0:
        print(s * 3)
    else:
        print(s)
    
    pr = s