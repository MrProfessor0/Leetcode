from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Solution 1
        # length = len(s) // 2
        # print(length)
        # for i in range(0,length):
        #     print(s[i],s[length-1-i])
        #     s[i],s[-1-i] = s[-1-i],s[i]

        # Solution 2
        s.reverse()

        print(s)


s = Solution()

n = ["h","e","l","l","o"]
s.reverseString(n)