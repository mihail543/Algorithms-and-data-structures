class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.max_levels = 0  

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.max_levels = 1
            return

        curr = self.root
        depth = 1

        while True:
            depth += 1
            if key < curr.data:
                if curr.left is None:
                    curr.left = Node(key)
                    if depth > self.max_levels:
                        self.max_levels = depth
                    break
                curr = curr.left
            elif key > curr.data:
                if curr.right is None:
                    curr.right = Node(key)
                    if depth > self.max_levels:
                        self.max_levels = depth
                    break
                curr = curr.right
            else:
                break

bst = BinarySearchTree()
f = True

while f:
    try:
        line = input()
        for el in line.split():
            x = int(el)
            if x == 0:
                f = False
                break
            bst.insert(x)
    except EOFError:
        break

print(bst.max_levels)
