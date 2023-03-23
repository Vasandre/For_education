# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/remove-linked-list-elements/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        answer = ListNode()
        otv = answer

        current = head

        while current:

            if current.val != val:
                answer.next = current
                answer = answer.next

            else:
                answer.next = current.next

            current = current.next

        return otv.next
