def swap_an(s1, s2):
    if len(s1) != len(s2):
        return "NO"

    counter = [0] * 36  

    for i in s1:
        if 'a' <= i <= 'z':
            counter[ord(i) - ord('a')] += 1
        else:  
            counter[26 + (ord(i) - ord('0'))] += 1

    for j in s2:
        if 'a' <= j <= 'z':
            counter[ord(j) - ord('a')] -= 1
        else:
            counter[26 + (ord(j) - ord('0'))] -= 1

    for k in counter:
        if k != 0:
            return "NO"

    return "YES"


n1 = input()
n2 = input()

print(swap_an(n1, n2))
