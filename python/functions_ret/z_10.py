def brackets(line):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    
    for char in line:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0