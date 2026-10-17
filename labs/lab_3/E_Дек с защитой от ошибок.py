class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        return self.items.pop(0)

    def pop_back(self):
        return self.items.pop()

    def front(self):
        return self.items[0]

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


d = Deque()

while True:
    parts = input().split()
    if not parts:
        continue

    command = parts[0]

    if command == 'push_front':
        d.push_front(int(parts[1]))
        print('ok')
        
    elif command == 'push_back':
        d.push_back(int(parts[1]))
        print('ok')
        
    elif command == 'pop_front':
        if d.is_empty():
            print('error')
        else:
            print(d.pop_front())
            
    elif command == 'pop_back':
        if d.is_empty():
            print('error')
        else:
            print(d.pop_back())
            
    elif command == 'front':
        if d.is_empty():
            print('error')
        else:
            print(d.front())
            
    elif command == 'back':
        if d.is_empty():
            print('error')
        else:
            print(d.back())
            
    elif command == 'size':
        print(d.size())
        
    elif command == 'clear':
        d.clear()
        print('ok')
        
    elif command == 'exit':
        print('bye')
        break
