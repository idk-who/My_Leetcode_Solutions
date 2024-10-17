class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, list(str(num))))       
        n = len(num)

        suff_arr = [-1]*n

        ma = -1

        for i in range(n-1, -1, -1):
            suff_arr[i] = ma
            ma = max(num[i], ma)

        for i in range(n):
            if suff_arr[i] > num[i]:
                ind = n-1
                while num[ind] != suff_arr[i]:
                    ind -= 1
                num[i], num[ind] = num[ind], num[i]
                break
            
        return int("".join(map(str, num)))
                
                
