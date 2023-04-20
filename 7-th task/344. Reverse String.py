https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reversing(s, left, right):

            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            return reversing(s, left + 1, right - 1)
        return reversing(s, 0, len(s) - 1)
