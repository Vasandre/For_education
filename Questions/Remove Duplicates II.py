# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def remove_dupl(nums):

    left = 0
    # right = 0

    for right in range(len(nums)):

        if nums[left] != nums[right] and right - left > 2:
            left += 2
            nums[left] = nums[right]

            print(left, right)

        elif nums[left] != nums[right] and right - left == 2:
            left = right
            nums[left] = nums[right]

        print(nums)

    return left + 1


print(remove_dupl([0,0,1,1,1,1,2,3,3]))