from heapq import heappush, heappop
class NumberContainers:

    def __init__(self):
        self.nu_in = defaultdict(list)
        self.in_nu = dict()
        self.nu_removed = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.in_nu:
            ele = self.in_nu[index]
            self.nu_removed[ele].add(index)
        self.in_nu[index] = number
        if index in self.nu_removed[number]:
            self.nu_removed[number].remove(index)
        heappush(self.nu_in[number], index)

    def find(self, number: int) -> int:
        ind = -1
        while self.nu_in[number]:
            temp = self.nu_in[number][0]
            if temp in self.nu_removed[number]:
                heappop(self.nu_in[number])
            else:
                ind = temp
                break
        
        return ind
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)