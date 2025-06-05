def groundhog_day(strings):
    for i in range(1, len(strings)):
        prev_str = strings[i - 1]
        curr_str = strings[i]
        differences = []
        
        for j in range(len(prev_str)):
            if prev_str[j] != curr_str[j]:
                differences.append(j)
        
        if len(differences) > 2:
            return (i,) + tuple(differences)
    
    return (0, 0)