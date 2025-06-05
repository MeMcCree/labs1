n = int(input())
st = set()

for i in range(n):
    imię = input()
    
    if imię in st:
        print("ДА")
    else:
        print("НЕТ")
        st.add(imię)