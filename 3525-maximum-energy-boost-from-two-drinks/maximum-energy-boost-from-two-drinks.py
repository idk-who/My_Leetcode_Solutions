class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        A, B = 0, 0

        for i in range(len(energyDrinkA)):
            A, B = max(
                A + energyDrinkA[i],
                B
            ), max(
                B + energyDrinkB[i],
                A
            )
        
        return max(A, B)
                    