https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def search(left, right):
            if left > right:
                return left
            
            mid = (left + right) // 2

            if isBadVersion(mid):
                return search(left, mid - 1)
            else:
                return search(mid + 1, right)
    
        return search(1, n)