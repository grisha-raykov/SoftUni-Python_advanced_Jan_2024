def is_balanced():
    s = input()
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "NO"
            if opening.index(stack.pop()) != closing.index(char):
                return "NO"
    if stack:
        return "NO"
    return "YES"

# Test the function
print(is_balanced())  # Output: YES or NO based on your input