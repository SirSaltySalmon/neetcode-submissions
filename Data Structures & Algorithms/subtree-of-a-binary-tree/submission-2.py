# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def isTreeIdentical(root1, root2):
            if root1 is None and root2:
                return False
            if root2 is None and root1:
                return False
            if root1 is None and root2 is None:
                return True
            if root1.val == root2.val:
                left = isTreeIdentical(root1.left, root2.left)
                right = isTreeIdentical(root1.right, root2.right)
                return left and right
            return False
        
        if isTreeIdentical(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )