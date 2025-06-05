def main():
    n = int(input())

    a = 1
    b = 1
    i = 2
    while b < n:
        c = b
        b = a + b
        a = c
        i += 1

    if b == n:
        print(i)
    else:
        print('НЕТ')


if __name__ == '__main__':
    main()