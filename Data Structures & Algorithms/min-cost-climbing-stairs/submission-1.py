class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # interesting. it is climbing stairs but answer is not straight forward
        # answer still relies on climbing the last two stairs!
        # you can't skip them. so solve the sub problems....
        # at a step, u get min cost of getting to step -1 or step -2.
        # then u work out if u should go from step -1 or step -2
        # when accounting for the cost.
        # from there u get min cost of current step.
        # use min cost of current step and min cost of step -1.
        # which then becomes the last two for next problem!
        # top of staircase is beyond last index...
        # start at 0 or 1...

        if len(cost) <= 2:
            return min(cost)
        cost_of_last_two = [0, 0]
        # if we can start at 0 or 1 cost to reach 0 or 1 is both 0

        i = 2
        cur_cost = 0
        while i <= len(cost):
            one_before = cost_of_last_two[1] + cost[i-1]
            two_before = cost_of_last_two[0] + cost[i-2]
            cur_cost = min(one_before, two_before)

            cost_of_last_two[0] = cost_of_last_two[1]
            cost_of_last_two[1] = cur_cost
            
            i += 1
        
        return cost_of_last_two[-1]

