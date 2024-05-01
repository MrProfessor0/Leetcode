from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalpha() or i.isnumeric())
        length = len(s) - 1
        t = ''.join(s[i] for i in range(length,-1,-1))
        return s == t

s = Solution()

T = "A man, a plan, a canal: Panama"

print(s.isPalindrome(T))