from math import sqrt
c = float(input())
def y(x):
    return x**2 + sqrt(x)

l = 0
r = 100_000
e = 0.000001
while abs(r - l) > e:
    m = (r+l)/2
    if y(m)<c:
        l = m
    else: r = m
    
print(l)
