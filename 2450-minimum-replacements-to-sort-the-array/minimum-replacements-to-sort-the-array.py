class Solution:
    def minimumReplacement(self, arr: List[int]) -> int:
        operations = 0
        mi = float("inf")
        for i in range(len(arr)-1, -1, -1):
            # print(mi)
            if arr[i] < mi:
                mi = arr[i]
            elif arr[i] > mi:
                partitions = (arr[i]//mi) + ((arr[i]%mi)!=0)
                operations += partitions - 1
                left_ele = arr[i]//partitions
                mi = left_ele
        return operations
            