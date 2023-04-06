# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        paren_dict = {"(": ")"}
        max_length_stack = 0

        for ch in s:
            if ch in paren_dict:
                stack.append(ch)
                if max_length_stack < len(stack):
                    max_length_stack = len(stack)
            else:
                if ch == ")":
                    stack.pop()

        return max_length_stack