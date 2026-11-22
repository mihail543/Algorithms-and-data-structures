import heapq as h

n = int(input())
numbers = []
while len(numbers) < n:
    numbers.extend(map(int, input().split()))

h.heapify(numbers)

summ = 0

while len(numbers) > 1:
    a = h.heappop(numbers)
    b = h.heappop(numbers)
    s = a + b
    summ += s
    h.heappush(numbers, s)

cost = summ * 0.05
print(f"{cost:.2f}")
