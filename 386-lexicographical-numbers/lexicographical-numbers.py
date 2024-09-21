class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        limit = n
        num = 1

        for _ in range(n):
            result.append(num)

            if num * 10 <= limit:
                num *= 10
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                num += 1
        
        return result

