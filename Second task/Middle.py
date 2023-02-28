# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        link = head

        if not link:
            return link

        length = 0
        numbers_node = []

        while link:
            length += 1
            numbers_node.append(link)
            link = link.next

        print(link)
        length = length // 2

        return numbers_node[length]