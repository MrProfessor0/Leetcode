from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        length = len(nums)
        for i in range(0,length):
            # print(nums)
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1

        print(nums)


nums = [0,1,0,3,12]
# nums = [0]

s = Solution()
s.moveZeroes(nums)