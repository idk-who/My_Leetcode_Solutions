class Solution:
    def sieve(self, n):
        nums = [True]*(n+1)
        nums[0] = False
        nums[1] = False

        for i in range(2, int(n**(1/2))+1):
            for j in range(i+i, n+1, i):
                nums[j] = False
                
        return nums

    def closestPrimes(self, left: int, right: int) -> List[int]:
        diff = float('inf')
        nums = (-1, -1)

        primes = self.sieve(right)

        prev = None

        for i in range(left, right+1):
            if primes[i]:
                if prev:
                    if i-prev < diff:
                        diff = i-prev
                        nums = (prev, i)
                prev = i
        
        return nums
        