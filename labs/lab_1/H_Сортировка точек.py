class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def farther(a, b):
    da = a.x * a.x + a.y * a.y
    db = b.x * b.x + b.y * b.y
    return da > db


def sort_points(points):
    n = len(points)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if farther(points[j], points[j + 1]):
                points[j], points[j + 1] = points[j + 1], points[j]


n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

sort_points(points)

for p in points:
    print(p.x, p.y)
