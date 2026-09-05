# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            #1. empty the queue
            cur_depth = queue
            queue = deque([])

            #2. get the rightmost in this depth
            res.append(cur_depth[-1].val)
            
            #3. get each child for next iteration
            for node in cur_depth:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
