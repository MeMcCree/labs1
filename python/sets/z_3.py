st1 = set(input())
st2 = set(input())
st3 = set(input())

wspólne = (st1 & st2) | (st1 & st3) | (st2 & st3)
print(''.join(wspólne))