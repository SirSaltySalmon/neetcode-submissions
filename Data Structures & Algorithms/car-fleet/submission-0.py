class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort the position and speed by position, backwards
        cars = sorted(zip(position, speed), reverse=True)
        
        res = 0
        fleet_leader = -1
        for i in range(len(cars)):
            # Check from closest car to destination first
            if fleet_leader != -1:
                time_for_current = (target - cars[i][0]) / cars[i][1]
                time_for_latest = (target - cars[fleet_leader][0]) / cars[fleet_leader][1]
                if time_for_current <= time_for_latest:
                    # is a fleet tgt
                    pass
                else:
                    # is not a fleet, so it will be the next leader!!!
                    res += 1
                    fleet_leader = i
            else:
                fleet_leader = i
        
        if fleet_leader != -1:
            res += 1
        
        return res