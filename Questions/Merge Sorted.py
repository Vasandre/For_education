# https://leetcode.com/problems/merge-sorted-array/

def sorts(nums1, m, nums2, n):

    first = m - 1
    second = m + n - 1
    third = n - 1


    while first >= m - n and third >= 0:

        if nums1[first] <= nums2[third]:
            nums1[second] = nums2[third]
            second -= 1
            third -= 1

        if nums2[third] < nums1[first]:
            nums1[second] = nums1[first]
            first -= 1
            second -= 1

    return nums1


print(sorts([2, 0], 1, [1], 1))
