n, k = map(int, input().split())
arr = list(map(int, input().split()))

deque = []
head = 0
for i in range(n):
    while len(deque) > head and arr[deque[-1]] >= arr[i]:
        deque.pop()
    deque.append(i)
    if deque[head] <= i - k:
        head += 1
    if i >= k - 1:
        print(arr[deque[head]])
