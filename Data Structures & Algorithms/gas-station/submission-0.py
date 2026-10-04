class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # find start where gas > cost... and continue from there
        # doesn't work? try to find a later start?
        # that is certain to be o(n^2)
        # see we can fix this, by seeing, at a certain starting station...
        # "hey, if i have started at this instead, id have more gas than now"
        # so greedily we choose to start there instead
        # but this only applies if we're in our first iteration
        # when we start looping to try and complete the circuit we already
        # checked every potential start
        # at most we cycle 2n times which is O(n)

        start = 0
        i = 0
        cur_gas = 0
        first_cycle = True
        while i < len(gas):
            if not first_cycle and i == start:
                break
            cur_gas += gas[i]
            if cur_gas < cost[i]:
                if not first_cycle:
                    return -1
                # well, our current or any previous i is not possible as a start...
                start = i + 1
                cur_gas = 0
                if start == len(gas):
                    return -1
            else:
                # cycle is okay so far!
                cur_gas -= cost[i]
            i += 1
            if i == len(gas) and first_cycle:
                first_cycle = False
                i = 0
        return start
