# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:

    def validPalindrome(self, s: str) -> bool:
        def val_pal(s, left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:
                return val_pal(s, l, r - 1) or val_pal(s, l + 1, r)

            l += 1
            r -= 1

        return True

