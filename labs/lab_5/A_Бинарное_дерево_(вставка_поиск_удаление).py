class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        elif not (node.left is None) and not (node.right is None):
            max_node = self._find_max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, node.data)
        elif not (node.left is None):
            node = node.left
        elif not (node.right is None):
            node = node.right
        else:
            node = None
        return node

    def _find_max_node(self, node):
        if node.right is None:
            return node
        return self._find_max_node(node.right)

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is None:
            return
        self._print_tree(node.left, level + 1)
        for _ in range(level):
            print(".", end="")
        print(node.data)
        self._print_tree(node.right, level + 1)

bst = BinarySearchTree()

while True:
    try:
        line = input().strip()
        if not line:
            continue
        
        parts = line.split()
        command = parts[0]
        
        if command == "ADD":
            n = int(parts[1])
            if bst.search(n):
                print("ALREADY")
            else:
                bst.insert(n)
                print("DONE")
                
        elif command == "DELETE":
            n = int(parts[1])
            if not bst.search(n):
                print("CANNOT")
            else:
                bst.delete(n)
                print("DONE")
                
        elif command == "SEARCH":
            n = int(parts[1])
            if bst.search(n):
                print("YES")
            else:
                print("NO")
                
        elif command == "PRINTTREE":
            bst.print_tree()
            
    except EOFError:
        break 
