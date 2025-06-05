n = int(input())
nz = False

ans = ''

if n == 0:
    ans = '0'

while n:
    c = n % 10
    
    if c != 0:
        nz = True
    
    if nz:
        ans += chr(ord('0') + c)

    n //= 10

print(ans)
