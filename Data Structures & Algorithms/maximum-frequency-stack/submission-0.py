class FreqStack:
    hashmap: dict
    groups: list
    max_freq: int

    def __init__(self):
        self.hashmap = {}
        self.groups = [[]]
        self.max_freq = 0

    def push(self, val: int) -> None:
        new_freq = self.hashmap.get(val, 0) + 1
        self.hashmap[val] = new_freq

        if new_freq > self.max_freq:
            self.groups.append([val])
            self.max_freq += 1
        else:
            self.groups[new_freq].append(val)

    def pop(self) -> int:
        top_freq_groups = self.groups.pop()
        val_to_return = top_freq_groups.pop()
        self.hashmap[val_to_return] -= 1

        if top_freq_groups:
            self.groups.append(top_freq_groups)
        else:
            self.max_freq -= 1
        
        return val_to_return
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()