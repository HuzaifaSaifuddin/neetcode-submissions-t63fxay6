# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        node1 = list1
        node2 = list2

        new_node = ListNode(-1)
        cur_node = new_node

        while node1 and node2:
            if node1.val <= node2.val:
                cur_node.next = node1
                node1 = node1.next
                cur_node = cur_node.next
            else:
                cur_node.next = node2
                node2 = node2.next
                cur_node = cur_node.next

        if node1:
            cur_node.next = node1

        if node2:
            cur_node.next = node2


        return new_node.next