from collections import deque

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))

left = deque()
right = deque()
for i in range(n):
    if arr[i][0] == '+':
        right.append(arr[i][1])
    if arr[i][0] == '*':
        left.append(arr[i][1])
    if arr[i][0] == '-':
        print(left.popleft())
    if len(left) < len(right):
        x = right.popleft()
        left.append(x)
    elif len(left) > len(right) + 1:
        x = left.pop()
        right.appendleft(x)
