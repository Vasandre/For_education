# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def count_lenght(start):

            len_node = 0

            while start:
                len_node += 1
                start = start.next

            return len_node

        def shift(distance, current):

            for _ in range(distance):
                current = current.next

            return current

        len_A = count_lenght(headA)
        len_B = count_lenght(headB)

        point_A = headA
        point_B = headB

        if len_A < len_B:
            point_B = shift(len_B - len_A, headB)
        else:
            point_A = shift(len_A - len_B, headA)

        while point_A:

            if point_A == point_B:
                return point_A

            point_A = point_A.next
            point_B = point_B.next

        return None
