import heapq

n = int(input())
arr = []
for i in range(n):
    t, l = map(int, input().split())
    arr.append((t, l))

arr.sort()
heap = []
mx = 0
for t, l in arr:
    while heap and heap[0] <= t:
        heapq.heappop(heap)
    heapq.heappush(heap, t + l)
    if len(heap) > mx:
        mx = len(heap)

print(mx)
