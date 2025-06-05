def horse(start, end):
    col_start = ord(start[0]) - ord('a') + 1
    col_end = ord(end[0]) - ord('a') + 1
    
    row_start = int(start[1])
    row_end = int(end[1])
    
    col_diff = abs(col_start - col_end)
    row_diff = abs(row_start - row_end)
    
    print((col_diff == 1 and row_diff == 2) or (col_diff == 2 and row_diff == 1))