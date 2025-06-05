def borders(top_left, bottom_right, point):
    x1, y1 = top_left
    x2, y2 = bottom_right
    px, py = point
    
    x_left, x_right = min(x1, x2), max(x1, x2)
    y_top, y_bottom = max(y1, y2), min(y1, y2)
    
    if (px == x_left or px == x_right) and y_bottom <= py <= y_top:
        print("AT THE EDGE")
        return

    if (py == y_top or py == y_bottom) and x_left <= px <= x_right:
        print("AT THE EDGE")
        return
    
    if x_left < px < x_right and y_bottom < py < y_top:
        print("INSIDE")
        return
    
    print("OUTSIDE")