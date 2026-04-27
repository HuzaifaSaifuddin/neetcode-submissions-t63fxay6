# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        curr = root
        parent = None

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return root

        if curr.left is None:
            if parent is None:
                return curr.right
            if parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right

        elif curr.right is None:
            if parent is None:
                return curr.left
            if parent.left == curr:
                parent.left = curr.left
            else:
                parent.right = curr.left

        else:
            # Find inorder successor
            successor = curr.right
            successor_parent = curr

            while successor.left:
                successor_parent = successor
                successor = successor.left

            curr.val = successor.val

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root