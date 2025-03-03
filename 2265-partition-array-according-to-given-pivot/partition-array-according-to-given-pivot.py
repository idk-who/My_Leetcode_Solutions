class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt = []
        gt = []
        same = []

        for i in nums:
            if i < pivot:
                lt.append(i)
            elif i > pivot:
                gt.append(i)
            else:
                same.append(i)
        
        return lt+same+gt