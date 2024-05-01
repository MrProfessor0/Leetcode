class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Character count array
        count1 = [0] * 26
        for i in range(len(s1)):
           index = ord(s1[i]) - ord('a')
           count1[index] += 1  

        # Traverse s2 string in window of size s1 length and compare;
        i=0
        window_size = len(s1)
        count2 = [0] * 26

        # running for first window
        while(i<window_size and i < len(s2)):
            index = ord(s2[i]) - ord('a')
            count2[index] += 1
            i += 1

        if count1 == count2:
            return True

        # print(i)

        while(i<len(s2)):
            newchar = s2[i]
            index = ord(newchar) - ord('a')
            count2[index] += 1

            oldchar = s2[i-window_size]
            index = ord(oldchar) - ord('a')
            count2[index] -= 1
            
            i += 1

            if count1 == count2:
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"

print(s1,s2)
s = Solution()
print(s.checkInclusion(s1,s2))