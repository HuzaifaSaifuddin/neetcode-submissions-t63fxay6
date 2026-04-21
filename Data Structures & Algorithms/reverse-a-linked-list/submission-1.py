# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head

        # Reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Fix current node
        head.next.next = head
        head.next = None

        return new_head