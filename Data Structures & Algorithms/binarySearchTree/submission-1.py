class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = Node(key, val)
            return

        current = self.root
        while True:
            if key == current.key:
                current.val = val
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, val)
                    return
                current = current.left
            else:  # key > current.key
                if current.right is None:
                    current.right = Node(key, val)
                    return
                current = current.right

    def get(self, key: int) -> int:
        if self.root == None:
            return -1

        current = self.root
        while current:
            if key == current.key:
                return current.val
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return -1

    def getMin(self) -> int:
        if self.root == None:
            return -1

        current = self.root
        while current.left:
            current = current.left

        return current.val

    def getMax(self) -> int:
        if self.root == None:
            return -1

        current = self.root
        while current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        if self.root is None:
            return

        current = self.root
        parent = None

        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            successor = current.right
            successor_parent = current

            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.key = successor.key
            current.val = successor.val

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def getInorderKeys(self) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.key)
            inorder(node.right)

        inorder(self.root)
        return result
