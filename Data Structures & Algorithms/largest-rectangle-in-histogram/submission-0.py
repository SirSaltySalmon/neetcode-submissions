class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # rectangle: min of height of all blocks * width
        max_area = 0 
        stack = []
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                # Then extending right is no longer beneficial.
                # Calculate all possible max rec heights, extending left
                # But also stop when extending left is no longer beneficial.
                h = heights[stack.pop()]
                # If stack is empty, it means 'h' was the smallest height so far
                # So it can span the whole histogram
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        return max_area
            