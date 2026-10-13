def sort1(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def sort2(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))

s = 0
for i in range(len(n1)):
    s+= sort1(n1)[i]*sort2(n2)[i]

print(s)
