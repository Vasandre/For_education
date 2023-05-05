# https://leetcode.com/problems/minimum-time-to-repair-cars/description/

import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        left = 0
        right = min(ranks) * (cars ** 2)

        while left < right:

            mid = (left + right) // 2
            count = 0

            for rank in ranks:
                count += math.floor((mid / rank) ** 0.5)
            
            if count < cars:
                left = mid + 1
            else:
                right = mid
        
        return left