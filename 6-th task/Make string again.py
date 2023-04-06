# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for ch in s:
            if stack and ((ord(stack[-1]) == ord(ch) + 32) or (ord(stack[-1]) + 32 == ord(ch))):
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)