def numerals(n):
    if not 0 <= n <= 100:
        return "Number out of range (0-100)"
    
    units = ["zero", "one", "two", "three", "four", 
             "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", 
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < 20:
        return units[n]
    elif n < 100:
        ten_part = tens[n // 10]
        unit_part = units[n % 10] if n % 10 != 0 else ""
        return f"{ten_part}-{unit_part}" if unit_part else ten_part
    else:
        return "one hundred"