class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0

        # Find local maximums
        while l < r and height[l+1] > height[l]:
            l += 1
        while r > l and height[r-1] > height[r]:
            r -= 1
        
        while l < r:
            l_potential = height[l]
            r_potential = height[r]
            # Does it meet a taller wall or a shorter wall???
            # Solution is, just iterate from the shorter wall,
            # Then you're guaranteed to meet a taller wall.
            if l_potential < r_potential:
                while height[l+1] < l_potential:
                    l += 1
                    result += l_potential - height[l]
                # When the while loop breaks we know we met
                # a taller or equal wall
                l += 1
            else:
                while height[r-1] < r_potential:
                    r -= 1
                    result += r_potential - height[r]
                r -= 1
        
        return result



        