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
        min_cost_to_reach = [0] * (len(cost)+1)
        # if we can start at 0 or 1 cost to reach 0 or 1 is both 0

        i = 2
        cur_cost = 0
        while i <= len(cost):
            cost_to_go_from_one_before = min_cost_to_reach[i-1] + cost[i-1]
            cost_to_go_from_two_before = min_cost_to_reach[i-2] + cost[i-2]
            min_cost_to_reach[i] = min(cost_to_go_from_one_before, cost_to_go_from_two_before)
            i += 1
        
        return min_cost_to_reach[-1]

