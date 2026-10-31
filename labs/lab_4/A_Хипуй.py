class MaxHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def insert(self, x):
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

    def extract(self):
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.sift_down(0)
            
        return max_val

n = int(input())
heap = MaxHeap()

for _ in range(n):
    command = input().split()
    
    if command[0] == '0':
        number = int(command[1])
        heap.insert(number)
    elif command[0] == '1':
        print(heap.extract())
