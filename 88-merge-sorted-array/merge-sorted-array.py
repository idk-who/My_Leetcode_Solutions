class Solution:
    def merge(self, nums1, m: int, nums2 , n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m -1
        j = n -1
        k = m+n-1

        while k>=0:
            print(k, i, j, nums1)
            if i<0 or j<0:
                break
            if nums1[i]>=nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k-=1
        while i>=0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1