n = int(input())

a = n // 1000
b = n % 1000 // 100
c = n % 100 // 10
d = n % 10

A = -1
B = -1
C = -1
D = -1

if a == 0 or b == 0 or c == 0 or d == 0:
    if A == -1:
        A = 0
    elif B == -1:
        B = 0
    elif C == -1:
        C = 0
    else:
        D = 0

if a == 1 or b == 1 or c == 1 or d == 1:
    if A == -1:
        A = 1
    elif B == -1:
        B = 1
    elif C == -1:
        C = 1
    else:
        D = 1

if a == 2 or b == 2 or c == 2 or d == 2:
    if A == -1:
        A = 2
    elif B == -1:
        B = 2
    elif C == -1:
        C = 2
    else:
        D = 2

if a == 3 or b == 3 or c == 3 or d == 3:
    if A == -1:
        A = 3
    elif B == -1:
        B = 3
    elif C == -1:
        C = 3
    else:
        D = 3

if a == 4 or b == 4 or c == 4 or d == 4:
    if A == -1:
        A = 4
    elif B == -1:
        B = 4
    elif C == -1:
        C = 4
    else:
        D = 4

if a == 5 or b == 5 or c == 5 or d == 5:
    if A == -1:
        A = 5
    elif B == -1:
        B = 5
    elif C == -1:
        C = 5
    else:
        D = 5

if a == 6 or b == 6 or c == 6 or d == 6:
    if A == -1:
        A = 6
    elif B == -1:
        B = 6
    elif C == -1:
        C = 6
    else:
        D = 6

if a == 7 or b == 7 or c == 7 or d == 7:
    if A == -1:
        A = 7
    elif B == -1:
        B = 7
    elif C == -1:
        C = 7
    else:
        D = 7

if a == 8 or b == 8 or c == 8 or d == 8:
    if A == -1:
        A = 8
    elif B == -1:
        B = 8
    elif C == -1:
        C = 8
    else:
        D = 8

if a == 9 or b == 9 or c == 9 or d == 9:
    if A == -1:
        A = 9
    elif B == -1:
        B = 9
    elif C == -1:
        C = 9
    else:
        D = 9

if A == 0:
    print(str(B) + str(A), str(D) + str(C))
else:
    print(str(A) + str(B), str(D) + str(C))    