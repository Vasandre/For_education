# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans = head
        point_1 = head
        point_2 = head.next
        summ = 0

        while point_2:

            if point_2.val != 0:
                summ += point_2.val

            elif point_2.val == 0 and point_2.next:
                point_1.val = summ
                point_1.next = point_2
                point_1 = point_1.next
                summ = 0

            else:
                point_1.val = summ
                point_1.next = None

            point_2 = point_2.next

        return ans
