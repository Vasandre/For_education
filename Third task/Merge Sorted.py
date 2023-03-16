# https://leetcode.com/problems/merge-sorted-array/

def sorts(nums1, m, nums2, n):

    first = m - 1
    second = n - 1

    if m == 0:
        nums1[m] = nums2[0]

    while first > 0:
        print(first, second)

        if nums1[first] < nums2[second]:
            nums1[m + second] = nums2[second]
            second -= 1

        else:
            nums1[first + 1] = nums1[first]
            nums1[first] = nums2[second]
            first -= 1


    return nums1


print(sorts([2, 0, 0], 1, [1, 1], 2))