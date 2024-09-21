class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def rec(num, limit):
            if num > limit:
                return
            result.append(num)
            for i in range(10):
                new_num = num*10 + i
                if new_num > limit: break
                rec(new_num, limit)

        for i in range(1, 10): 
            rec(i, n)
            
        return result