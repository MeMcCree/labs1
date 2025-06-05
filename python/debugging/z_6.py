from math import log2, ceil


def main():
    n = int(input())

    if n == 0:
        print(1)
        return

    lg = ceil(log2(n))
    mask = 1
    i = 0
    ans = 0
    while i < lg:
        if not (n & mask):
            ans += mask

        i += 1
        mask <<= 1

    print(ans)


if __name__ == '__main__':
    main()