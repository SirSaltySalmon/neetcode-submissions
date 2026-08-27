# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the node in question via recursion so 
        # i can reconnect the pointer to the parent easier
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: zero or one child, can replace with None or child
            if not root.right and not root.left:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            
            # case 2: two child. so replace by finding min of right subtree,
            # or max of left subtree, which will be replacements that
            # can fit right in.
            min_of_right = self.findMinNode(root.right)
            root.right = self.deleteNode(root.right, min_of_right.val)
            # should be deleted, cause we don't want any more references to it,
            root.val = min_of_right.val
        return root
        
    def findMinNode(self, root: Optional[TreeNode]):
        curr_node = root
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node
