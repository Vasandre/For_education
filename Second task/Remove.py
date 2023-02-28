# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        following = head.next
        previous = head

        while following is not None:

            if previous.val == following.val:
                previous.next = following.next
                following = following.next

            else:
                following = following.next
                previous = previous.next

        return head
