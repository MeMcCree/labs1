def horse2(position):
    col = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    
    moves = [
        (2, 1), (2, -1),
        (-2, 1), (-2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    
    possible_moves = []
    for dc, dr in moves:
        new_col = col + dc
        new_row = row + dr
        
        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            letter = chr(ord('a') + new_col - 1)
            possible_moves.append(f"{letter}{new_row}")
    
    for move in possible_moves:
        print(move)