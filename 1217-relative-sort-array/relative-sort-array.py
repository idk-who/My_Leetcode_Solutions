class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        comparator = {num:i for i, num in enumerate(arr2)} 
        return sorted(arr1, key=lambda x: (comparator.get(x, 1001), x))