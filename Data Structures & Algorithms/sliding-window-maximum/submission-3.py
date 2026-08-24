class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        R = 0
        res = [0] * (len(nums) - k + 1)
        initial_max = float("-inf")
        index_of_initial_max = 0
        queue = []
        while R < k:
            while queue and queue[-1][0] < nums[R]:
                queue.pop()
            queue.append([nums[R], R])
            R += 1
        
        res[0] = queue[0][0]
        R -= 1

        while R < len(nums) - 1:
            L += 1
            if queue[0][1] < L:
                queue.pop(0)
            
            R += 1
            while queue and queue[-1][0] < nums[R]:
                queue.pop()
            queue.append([nums[R], R])

            res[L] = queue[0][0]

        return res