# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 0 (1) -> 1 (2) -> 2 (3) -> 3 (None)

        # curr_node 0
        # prev_node None
        # curr_node_next 1

        node = head
        prev_node = None

        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return prev_node
