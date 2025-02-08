from heapq import heappush, heappop
class NumberContainers:

    def __init__(self):
        self.in_nu = dict()
        self.nu_in = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.in_nu[index] = number
        heappush(self.nu_in[number], index)

    def find(self, number: int) -> int:
        while self.nu_in[number]:
            ind = self.nu_in[number][0]
            if self.in_nu[ind] != number:
                heappop(self.nu_in[number])
            else:
                return ind
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)