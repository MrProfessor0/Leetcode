class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while(part in s):
            s = s.replace(part,"",1)
        return s        

T = "daabcbaabcbc"
part = "abc"

T = "aabababa"
part = "aba"

s = Solution()
print(s.removeOccurrences(T,part))