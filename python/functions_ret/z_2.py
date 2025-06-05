def rounding(numbers):
    sum_int = 0
    sum_frac = 0.0
    
    for num in numbers:
        integer_part = int(num)
        fractional_part = num - integer_part
        
        sum_int += integer_part
        sum_frac += fractional_part
    
    sum_frac_rounded = round(sum_frac, 2)
    
    return (sum_int, 0 if sum_frac_rounded == 0 else sum_frac_rounded)