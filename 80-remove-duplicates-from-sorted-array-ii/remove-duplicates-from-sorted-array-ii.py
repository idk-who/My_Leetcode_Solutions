class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        limit = 2
        # if len(nums)<3:
        #     return len(nums)
            
        while j<len(nums):
            """
            NOTE_ -> i++ includes nums[i] = nums[j]

            cases for i&j:
                i!=j -> DO i++, j++, limit = 2
                i==j -> DO j++, limit -= 1, POSSIBLE i++ based on limit var

            cases for limit:
                limit == 2 -> DO nothing
                limit == 1 -> DO nothing
                limit == 0 -> ALLOW i++

            Total cases:
            CASE 1: i!=j -> DO i++, j++, limit = 2 
            CASE 2: i==j
                CASE 2.1/2.2: limit = 2/1 -> DO i++, j++, limit--
                CASE 2.3: limit = 0 -> DO j++
            """
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j] 
                limit = 2
            else: #nums[i] == nums[j]
                if limit > 1 and i<j:
                    i+=1
                    nums[i] = nums[j]
                    limit -= 1
            j+=1

        return i+1

        