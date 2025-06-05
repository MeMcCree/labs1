def average(marks):
    if (not len(marks)):
        print(0)
        return
    print(sum(marks) / len(marks))