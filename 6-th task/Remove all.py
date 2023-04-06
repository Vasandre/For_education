# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for ch in s:

            if not stack:
                stack.append(ch)
            elif ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)