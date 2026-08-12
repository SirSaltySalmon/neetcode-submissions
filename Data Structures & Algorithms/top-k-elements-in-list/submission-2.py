class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]
        #one bucket for each possible length
        #so 1 to len(nums)
        #which is not 0 indexed

        for num in nums:
            count[num] = 1 + count.get(num, -1)
            #So to make it 0 indexed, we make the default value -1
        
        for key, value in count.items(): #Syntax for getting both key and value
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1): #start, stop, step
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res