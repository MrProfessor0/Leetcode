class Solution:
    def removeDuplicates(self, s: str) -> str:
        #Solution 1 gives TLE 
        # Flag = True
        # while(Flag):
        #     Flag = False
        #     for i in range(0,len(s)-1):
        #         if s[i] == s[i+1]:
        #             s=s[:i]+s[i+2:]
        #             Flag = True
        #             break

        # temp = ""
        # i = 0
        # while(i<len(s)):
        #     if s[i] == temp[-1:]:
        #         temp = temp[:-1]
        #     else:
        #         temp = temp+s[i]
        #     i+=1

        temp = []
        temp.append(s[0])
        i = 1
        while(i<len(s)):
            print(temp)
            if s[i] == "".join(temp[-1:]):
                temp.pop()
            else:
                temp.append(s[i])
            i+=1


        print( "".join(temp))


T = "abbaca"

print(T)
s=Solution()
s.removeDuplicates(T)