n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    c = []
    if l < n:
        c.append(a[l])
    if l > 0:
        c.append(a[l - 1])

    best = c[0]
    for val in c[1:]:
        if abs(val - x) <= abs(best - x):
            best = val
        elif abs(val - x) == abs(best - x) and val < best:
            best = val

    print(best)
