# https://leetcode.com/problems/remove-element/

def removeElement(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:

        if nums[left] == val and nums[right] == val:
            right -= 1

        elif nums[left] == val and nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        elif nums[left] != val:
            left += 1

    return left

