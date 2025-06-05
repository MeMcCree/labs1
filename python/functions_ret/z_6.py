def vowels_in_string(line):
    russian_vowels = 'аяоёуюэеыи'
    english_vowels = 'aeuioy'
    
    vowels = []
    for char in line:
        if char.lower() in russian_vowels or char.lower() in english_vowels:
            vowels.append(char)
    return vowels