while True:
    n = int(input())
    
    if not n:
        break
    
    if n % 3 == 0 and n % 7 == 0:
        print('Караул!')
        break
    elif n % 3 == 0:
        print('несчастливое')
    elif n % 7 == 0:
        print('опасное')
    else:
        print(n)