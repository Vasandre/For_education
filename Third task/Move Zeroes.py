# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        length = len(nums)

        while right < length:

            print(left, right)

            while nums[left] != 0 and left < right:
                left += 1
                # right += 1

            if nums[right] != 0 and nums[left] == 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1

            right += 1