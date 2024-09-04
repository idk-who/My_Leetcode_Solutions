class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def countPairs(arr, l, m, r):
            cnt = 0
            p1 = l
            p2 = m+1
            while p1 <= m and p2 <= r:
                if arr[p1] > 2 * arr[p2]:
                    cnt += (m - p1 + 1)
                    p2 += 1
                else:
                    p1 += 1
            return cnt

        def mergeSort(arr, l, r):
            if l >= r: return 0
            m = (l+r)//2
            cnt = mergeSort(arr, l, m)
            cnt += mergeSort(arr, m+1, r)
            cnt += countPairs(arr, l, m, r)
            arr[l:r+1] = sorted(arr[l:r+1])

            return cnt

        ans = mergeSort(nums, 0, len(nums)-1)
        print(nums)
        return ans