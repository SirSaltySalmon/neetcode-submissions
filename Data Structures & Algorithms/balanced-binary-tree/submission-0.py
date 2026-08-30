# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), _get_type_hints_obj_allowed_types:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if root is None:
                return 0
            
            return max(getHeight(root.left), getHeight(root.right)) + 1
        
        if root is None:
            return True
        
        height_left = getHeight(root.left)
        height_right = getHeight(root.right)
        balanced = abs(height_left - height_right) <= 1
        return (balanced and
                self.isBalanced(root.left) and
                self.isBalanced(root.right)
        )