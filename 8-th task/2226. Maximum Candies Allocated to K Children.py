# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        left = 1
        right = max(candies)
        ans = 0


        while left <= right:

            mid = (left + right) // 2
            if mid == 0:
                return 0

            count = 0

            for candie in candies:
                count += candie // mid

            if count >= k:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1

        return ans