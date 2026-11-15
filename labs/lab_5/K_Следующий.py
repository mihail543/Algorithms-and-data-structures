# Превышено максимальное время работы
class Node:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
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
                break

    def next(self, key):
        res = -1
        curr = self.root
        
        while curr is not None:
            if curr.data >= key:
                res = curr.data
                curr = curr.left
            else:
                curr = curr.right
                
        return res


n = int(input())

bst = BinarySearchTree()

last_op = None
last_y = 0

for _ in range(n):
    line = input().split()
    op = line[0]
    val = int(line[1])
    
    if op == '+':
        if last_op == '?':
            val = (val + last_y) % 10**9
        
        bst.insert(val)
        last_op = '+'
        
    else:
        ans = bst.next(val)
        print(ans)
        last_y = ans
        last_op = '?'
