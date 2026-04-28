# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def tree(node, arr=[]):
            if node is None:
                return arr

            left = tree(node.left, arr)
            arr.append(node.val)
            right = tree(node.right, arr)

            return arr

        arr = tree(root)

        return arr[k - 1]

        return -1
