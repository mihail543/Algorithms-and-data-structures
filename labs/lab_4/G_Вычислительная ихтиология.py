class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def insert(self, x):
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

    def extract(self):
        min_val = self.heap[0]
        last_val = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_val
            self.sift_down(0)
            
        return min_val


n = int(input())
aq = []
for _ in range(n):
    aq.append(int(input()))

heap = MinHeap()

for i in range(n):
    time_to_birth = max(1000 - aq[i], 1)
    popx_after = aq[i] + 1
    heap.insert((time_to_birth, i + 1, popx_after))

cur_time = 0
cur_pos = 1
ans = -1

while not heap.is_empty():
    next_time, target_aq, popx = heap.extract()
    travel_time = abs(cur_pos - target_aq)
    if cur_time + travel_time > next_time:
        ans = next_time
        break
    cur_time = next_time
    cur_pos = target_aq
    wait_time = max(1000 - popx, 1)
    next_time = cur_time + wait_time
    next_popx = popx + 1
    heap.insert((next_time, target_aq, next_popx))

print(ans)
