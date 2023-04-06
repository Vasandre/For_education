# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        paren_dict = {"(": ")", "[": "]", "{": "}"}

        for ch in s:

            if ch in paren_dict:
                stack.append(ch)

            else:
                if len(stack) == 0 or ch != paren_dict[stack.pop()]:
                    return False

        return len(stack) == 0