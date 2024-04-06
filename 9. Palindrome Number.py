class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while(temp):
            rev = (rev*10) + (temp%10)
            temp = int(temp/10)
        
        if rev == x:
            return True
        return False

s = Solution()
print(s.isPalindrome(int(input())))