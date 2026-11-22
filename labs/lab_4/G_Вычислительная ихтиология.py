import heapq

n = int(input())
aq = []
for _ in range(n):
    aq.append(int(input()))

heap = []
for i in range(n):
    time_to_birth = max(1000 - aq[i], 1)
    popx_after = aq[i] + 1
    heapq.heappush(heap, (time_to_birth, i + 1, popx_after))

cur_time = 0
cur_pos = 1
ans = -1

while heap:
    next_time, target_aq, popx = heapq.heappop(heap)
    travel_time = abs(cur_pos - target_aq)
    if cur_time + travel_time > next_time:
        ans = next_time
        break
    cur_time = next_time
    cur_pos = target_aq
    wait_time = max(1000 - popx, 1)
    next_time = cur_time + wait_time
    next_popx = popx + 1
    heapq.heappush(heap, (next_time, target_aq, next_popx))

print(ans)
