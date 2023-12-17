class RandomizedSet:

    def __init__(self):
        self.data = []
        self.dic  = dict()

    def insert(self, val: int) -> bool:
        if self.dic.get(val, -1) == -1:
            self.data.append(val)
            self.dic[val] = len(self.data)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        ind = self.dic.get(val, -1)
        if ind>-1:
            
            temp = self.data[-1]
            self.data[ind] = temp
            self.dic[temp] = ind

            del self.dic[val]
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()