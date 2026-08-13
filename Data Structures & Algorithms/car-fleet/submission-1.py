class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        latest_time = 0
        # I was wondering why someone would use a stack instead of this.
        # Because it's functionally the same.
        # And it is.
        # To replicate the stack's efficiency, I store the latest time instead

        for p, s in cars:
            time = (target - p) / s

            if time > latest_time:
                fleets += 1
                latest_time = time

        return fleets