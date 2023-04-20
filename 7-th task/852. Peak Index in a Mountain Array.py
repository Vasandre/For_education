https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def bin_search(mas, mid):

            if (mas[mid] > mas[mid - 1]) and (mas[mid] > mas[mid + 1]):
                return mid
            
            if mas[mid] > mas[mid - 1]:
                return bin_search(mas, mid + 1)
            else:
                return bin_search(mas, mid - 1)
        
        return bin_search(arr, (len(arr) - 1) // 2)