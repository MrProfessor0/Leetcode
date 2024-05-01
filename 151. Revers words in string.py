# class Solution:
#     def reverseWords(self, s: str) -> str:
#         temp = []
#         t = ''
#         length = len(s)

#         for i in range(length):
#             if s[i] != ' ':
#                 t = t + s[i]
#             elif t != "":
#                 temp.append(t)
#                 t = ""

#         # temp = temp.strip()
#         print(f"\'{' '.join(i for i in temp.reverse())}\'")

        

# T = "the sky is blue"
# # T = "  hello world  "
# # T = "example   good a"


# s = Solution()
# s.reverseWords(T)
