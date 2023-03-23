# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = ListNode(0)
        head = current

        point_1 = list1
        point_2 = list2

        while point_1 and point_2:

            if point_1.val < point_2.val:
                current.next = point_1
                point_1 = point_1.next
                current = current.next

            else:
                current.next = point_2
                point_2 = point_2.next
                current = current.next

        while point_1:
            current.next = point_1
            point_1 = point_1.next
            current = current.next

        while point_2:
            current.next = point_2
            point_2 = point_2.next
            current = current.next

        return head.next
