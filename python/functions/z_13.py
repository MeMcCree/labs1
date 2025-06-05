def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 1:
        print(sorted_numbers[mid])
    else:
        print((sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2)