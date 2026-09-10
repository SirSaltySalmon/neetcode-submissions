# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        all_nodes = []

        def in_order(node):
            nonlocal all_nodes
            if node is None:
                return
            in_order(node.left)
            all_nodes.append(node)
            in_order(node.right)
        
        in_order(root)

        return all_nodes[k-1].val