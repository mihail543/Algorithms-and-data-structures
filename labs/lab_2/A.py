N, K = map(int, input().split())
n = list(map(int, input().split()))
k = list(map(int, input().split()))

for x in k:
    l = 0
    r = N - 1
    f = False
    while l <= r:
        mid = (l + r) // 2
        if n[mid] == x:
            f = True
            break
        elif n[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    print('YES' if f else 'NO')
