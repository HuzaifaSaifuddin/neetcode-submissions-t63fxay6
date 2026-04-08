class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> int:
        if self.tail == None:
            return -1

        current_tail = self.tail
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return current_tail.value
        else:
            self.tail = current_tail.prev
            self.tail.next = None
            return current_tail.value
            

    def popleft(self) -> int:
        if self.head == None:
            return -1

        current_head = self.head
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return current_head.value
        else:
            self.head = current_head.next
            self.head.prev = None
            return current_head.value
