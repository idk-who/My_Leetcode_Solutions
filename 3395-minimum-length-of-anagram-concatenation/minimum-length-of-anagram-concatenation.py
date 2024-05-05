from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        # Get the length of the input string 's'
        n = len(s)

        # Define a helper function to calculate the greatest common divisor (GCD)
        def gcd(a, b):
            # Euclidean algorithm to find GCD
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a

        # Count the occurrences of each character in 's' using Counter
        hashmap = Counter(s)

        # Initialize the divisor with the count of the first character in 's'
        div = hashmap[s[0]]

        # Iterate over the counts of characters in the hashmap
        for key, value in hashmap.items():
            # Update the divisor by finding the GCD of the current count and the previous divisor
            div = gcd(div, value)
        
        # Return the minimum length of 't', which is the length of 's' divided by the divisor
        return n // div