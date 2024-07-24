class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def custom(num):
            return int("".join(map(lambda x: str(mapping[int(x)]), list(str(num)))))
        
        nums.sort(key = custom)
        return nums