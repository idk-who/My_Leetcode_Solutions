class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums.sort(key = lambda x: x > pivot)
        nums.sort(key = lambda x: x < pivot, reverse=True)
        return nums