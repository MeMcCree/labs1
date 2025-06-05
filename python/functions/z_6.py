def line(x1, y1, x2, y2):    
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    
    k_rounded = round(k, 2)
    b_rounded = round(b, 2)
    
    if b_rounded < 0:
        sign = '-'
        b_abs = abs(b_rounded)
    else:
        sign = '+'
        b_abs = b_rounded
    
    equation = f"y = {round(0.0, 2) if k_rounded == 0.0 else k_rounded} * x {sign} {b_abs}"
    
    if b_rounded == 0:
        equation = f"y = {k_rounded} * x"
    
    print(equation)