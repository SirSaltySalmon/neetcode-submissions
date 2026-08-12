class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        
        # The only reason moving in is beneficial is if moving in gives you a
        # taller height. if l is taller than r, r moves in to attempt to grow.

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            # But what if they're the same?

        
        return res