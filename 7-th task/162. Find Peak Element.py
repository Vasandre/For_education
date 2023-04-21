class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search(mas, left, right):

          if left == right:
            return left

          mid = (left + right) // 2

          if mas[mid] < mas[mid + 1]:
              return bin_search(mas, mid + 1, right)
          else:
              return bin_search(mas, left, mid)

        return bin_search(nums, 0, len(nums) - 1)