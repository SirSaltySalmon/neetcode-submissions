# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # well, lowest common ancestor is the lowest number
        # that is still in between or equal to the two number.
        # let's make sure p is a lower bound first
        if p.val > q.val:
            p, q = q, p
        
        res = root

        def search(node):
            nonlocal res
            cur = node

            while cur.val > q.val or cur.val < p.val:
                if cur.val > q.val:
                    cur = cur.left
                else:
                    cur = cur.right
            
            res = cur
            # now we're in range.
            # but we've no guarantee this is the lowest
            # actually we do have a guarantee and that's crazy
        
        search(root)
        return res

        
