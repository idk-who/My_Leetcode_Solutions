class ProductOfNumbers:
    def __init__(self):
        self.sum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.sum = [1]
        else:
            self.sum.append(self.sum[-1]*num)
        
    def getProduct(self, k: int) -> int:
        if len(self.sum) <= k: return 0
        return self.sum[-1]//self.sum[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)