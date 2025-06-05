def permission(code):
    code_sum = sum(int(digit) for digit in str(code))

    secret_sum = sum(int(digit) for digit in input())
    
    if code_sum == secret_sum:
        print("ACCESS IS ALLOWED")
    else:
        print("ACCESS IS DENIED")