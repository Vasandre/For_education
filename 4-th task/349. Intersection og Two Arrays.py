def intersection(nums1, nums2):
    point_1 = 0

    answer = []

    while point_1 < len(nums1):
        point_2 = 0
        while point_2 < len(nums2):

            if nums1[point_1] == nums2[point_2] and nums1[point_1] not in answer:
                answer.append(nums1[point_1])
            point_2 += 1

        point_1 += 1

    return answer

