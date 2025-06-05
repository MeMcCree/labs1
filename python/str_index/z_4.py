def main():
    linia = input()

    for i in range(1, len(linia)):
        if linia[i] < linia[i - 1]:
            print(linia[i])
            return
    
    print("(:_0_:)")


if __name__ == "__main__":
    main()