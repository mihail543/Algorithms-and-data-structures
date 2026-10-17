class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def top(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


q = Queue()

while True:
    parts = input().split()

    if not parts:
        continue

    command = parts[0]

    if command == 'push':
        n = int(parts[1])
        q.push(n)
        print('ok')

    elif command == 'pop':
        if q.is_empty():
            print('error')
        else:
            print(q.pop())

    elif command == 'front':
        if q.is_empty():
            print('error')
        else:
            print(q.top())

    elif command == 'size':
        print(q.size())

    elif command == 'clear':
        q.clear()
        print('ok')

    elif command == 'exit':
        print('bye')
        break
