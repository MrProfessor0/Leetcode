from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        length = len(nums)

        for i in range(1,length):
            if nums[i-1] > nums[i]:
                count += 1
                continue
        
        if nums[length-1] > nums[0]:
            count += 1

        return count <= 1

nums = [3,4,5,1,2]

s = Solution()
print(s.check(nums))