class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        def BS(word):
            l = 0 
            r = len(products)

            while l < r:
                m = l + (r-l)//2
                if word <= products[m]:
                    r = m
                else:
                    l = m + 1
            
            return l
        
        ans = []

        temp = ''
        for c in searchWord:
            temp += c

            ptr = BS(temp)

            lst = []

            while len(lst) < 3 and ptr < len(products) and products[ptr].startswith(temp):
                lst.append(products[ptr])
                ptr += 1
            
            ans.append(lst)
        
        return ans
