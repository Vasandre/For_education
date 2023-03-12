# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            current = 0
            movable = 0

            while movable < len(nums):

                if nums[current] != nums[movable]:
                    current += 1
                    nums[current] = nums[movable]

                movable += 1

            return current + 1