# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            nonlocal pre_idx

            # base case
            if left > right:
                return None

            # 1. pick root
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            # 2. split inorder
            mid = inorder_index[root_val]

            # 3. build left subtree
            root.left = helper(left, mid - 1)

            # 4. build right subtree
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)