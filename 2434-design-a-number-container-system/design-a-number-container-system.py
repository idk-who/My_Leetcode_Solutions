from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.in_nu = dict()
        self.nu_in = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.in_nu:
            prev_nu = self.in_nu[index]
            self.nu_in[prev_nu].remove(index)
        self.in_nu[index] = number
        self.nu_in[number].add(index)
        
    def find(self, number: int) -> int:
        if len(self.nu_in[number]) == 0:
            return -1
        return self.nu_in[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)