# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(len(nums)):
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1

        return left
