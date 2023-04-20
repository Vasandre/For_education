https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums, target, left, right):
            if right >= left:
                
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    return bin_search(nums, target, left, mid-1)
                else:
                    return bin_search(nums, target, mid+1, right)
            else:
                return -1

        return bin_search(nums, target, 0, len(nums)-1)