class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.sum = []

    def add(self, num: int) -> None:
        self.data.append(num)
        if len(self.sum) >= 1:
            self.sum.append(self.sum[-1]*num)
        else:
            self.sum.append(num)
        if num == 0:
            self.sum = []
        
    def getProduct(self, k: int) -> int:
        if len(self.sum) < k: return 0
        if len(self.sum) == k: return self.sum[-1]
        return self.sum[-1]//self.sum[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)