class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = dict()
        
        def rec(books, max_width, ptr, curr_width, max_height, dp):
            if ptr == len(books):
                return max_height
            
            if (ptr, curr_width) in dp:
                return dp[(ptr, curr_width)]
            
            mi = float("inf")
            if curr_width+books[ptr][0] <= max_width:
                mi = min(
                    mi, rec(
                        books, max_width, 
                        ptr+1, 
                        curr_width+books[ptr][0], 
                        max(max_height, books[ptr][1]),
                        dp
                        )
                    )
            mi = min(
                mi,
                max_height + 
                rec(
                    books, max_width, 
                    ptr+1, 
                    books[ptr][0], 
                    books[ptr][1],
                    dp
                )
            )

            dp[(ptr, curr_width)] = mi

            return mi

        return rec(books, shelfWidth, 0, 0, 0, dp)