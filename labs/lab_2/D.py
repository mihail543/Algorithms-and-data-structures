a, b, c, d = map(int, input().split())

def y(x):
    return a*x**3 + b*x**2 + c*x + d


l = -100000
r = 100000
e = 0.00000001

while r - l > e:
    m = (l + r) / 2
    if y(m) * y(l) <= 0:
        r = m
    else:
        l = m
print(l)
