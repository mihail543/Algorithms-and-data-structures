def correct_bracket_sequence(st):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in st:
        if ch not in '}{[]()':
            continue
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

s = input()
print('yes' if correct_bracket_sequence(s) else 'no')
