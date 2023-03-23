# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse_half(start):
            current = start
            previous = None

            while current:
                follow = current.next
                current.next = previous

                previous = current
                current = follow

            return previous

        left = head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = reverse_half(slow)

        while right:

            if left.val != right.val:
                return False

            right = right.next
            left = left.next

        return True
