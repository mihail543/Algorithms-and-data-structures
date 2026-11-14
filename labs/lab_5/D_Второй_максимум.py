class Node:
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

    def second_max(self):
        stack = []
        curr = self.root
        count = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            count += 1

            if count == 2:
                return curr.data

            curr = curr.left

        return None


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

print(bst.second_max())
