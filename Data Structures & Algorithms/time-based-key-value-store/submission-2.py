from collections import defaultdict

class TimeMap:
    hashmap: dict

    def __init__(self):
        self.hashmap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        stamps = self.hashmap[key]
        if not stamps or stamps[0][0] > timestamp:
            return ''
        l = 0
        r = len(stamps) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if stamps[mid][0] > timestamp:
                r = mid - 1
            elif stamps[mid][0] < timestamp:
                l = mid
            else:
                l = mid
                r = mid
        
        pair = stamps[l]
        return pair[1]
        
