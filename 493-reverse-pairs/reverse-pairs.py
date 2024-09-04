class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr, l, m, r):
            L = arr[l:m+1]
            R = arr[m+1:r+1]

            p1 = 0
            p2 = 0
            p3 = l

            while p1 < len(L) and p2 < len(R):
                if L[p1] < R[p2]:
                    arr[p3] = L[p1]
                    p1 += 1
                else:
                    arr[p3] = R[p2]
                    p2 += 1    
                p3 += 1
            while p1 < len(L):
                arr[p3] = L[p1]
                p1 += 1
                p3 += 1
            while p2 < len(R):
                arr[p3] = R[p2]
                p2 += 1
                p3 += 1

        def mergeSort(arr, l, r):
            if l >= r: return 0

            m = (l+r)//2
            cnt = mergeSort(arr, l, m)
            cnt += mergeSort(arr, m+1, r)
            
            p1 = l
            p2 = m+1

            while p1 <= m and p2 <= r:
                if arr[p1] > 2 * arr[p2]:
                    cnt += (m - p1 + 1)
                    p2 += 1
                else:
                    p1 += 1

            merge(arr, l, m, r)

            return cnt

        ans = mergeSort(nums, 0, len(nums)-1)
        print(nums)
        return ans