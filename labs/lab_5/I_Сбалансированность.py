class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 0


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

    def is_balanced(self):
        if self.root is None:
            return True

        stack = [(self.root, False)]

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                left_h = node.left.height if node.left else 0
                right_h = node.right.height if node.right else 0

                if abs(left_h - right_h) > 1:
                    return False

                node.height = 1 + max(left_h, right_h)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return True


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

print("YES" if bst.is_balanced() else "NO")
