# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        link = head
        numbers = []

        while link:
            numbers.append(link.val)
            link = link.next

        if numbers == numbers[::-1]:
            return True
        else:
            return False