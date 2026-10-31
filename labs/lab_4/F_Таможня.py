class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

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


arr = []
for _ in range(n):
    t, l = map(int, input().split())
    arr.append((t, l))
        
arr.sort()
    
heap = MinHeap()
mx = 0
    
for t, l in arr:
    while not heap.is_empty() and heap.heap[0] <= t:
        heap.extract()
            
    heap.insert(t + l)
        
    if heap.size() > mx:
        mx = heap.size()
            
print(mx)
