import random

class Node:
    __slots__ = ('data', 'left', 'right', 'cnt')
    
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.cnt = 1

class BinarySearchTree:
    __slots__ = ('root',)
    
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        curr = self.root
        while True:
            if key < curr.data:
                if curr.left is None:
                    curr.left = Node(key)
                    break
                curr = curr.left
            elif key > curr.data:
                if curr.right is None:
                    curr.right = Node(key)
                    break
                curr = curr.right
            else:
                curr.cnt += 1
                break

    def enter(self):
        result = []
        curr = self.root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(f"{curr.data} {curr.cnt}")
            curr = curr.right
        return result

data = []
for el in open(0).read().split():
    x = int(el)
    if x == 0:
        break
    data.append(x)

random.shuffle(data)

bst = BinarySearchTree()
for x in data:
    bst.insert(x)

ans = bst.enter()
if ans:
    print('\n'.join(ans))
