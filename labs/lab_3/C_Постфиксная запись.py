def postfix_notation(a):
    steck = []
    for ch in a:
        if ch in '+-*/':
            x2 = steck.pop()
            x1 = steck.pop()
            x3 = eval(str(x1)+str(ch)+str(x2))
            steck.append(x3)
        else:
            steck.append(int(ch)) 
    return steck[0]

postfix = input()
list_postfix = list(s for s in postfix.split())
print(postfix_notation(list_postfix))
