from typing import List, Optional

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[Node] = None

class LinkedList:
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
    
    def get(self, index: int) -> int:
        count = 0
        node = self.head
        while count < index and node:
            node = node.next
            count += 1
        
        if node:
            return node.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        count = 0
        node = self.head
        while count < index - 1 and node.next:
            node = node.next
            count += 1

        if node.next is None:
            return False

        node.next = node.next.next

        if node.next is None:
            self.tail = node

        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node:
            values.append(node.val)
            node = node.next
        return values