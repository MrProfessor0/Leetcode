from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        length = len(nums)
        temp = [None] * length

        for i in range(0,length):
            temp[(i+k)%length] = nums[i]
        # nums = temp
        print(nums)
        print(temp)

        # Solution 2
        # One line of thought is based on reversing the array (or parts of it) to obtain the desired result. 
        # Think about how reversal might potentially help us out by using an example.


# nums = [1,2,3,4,5,6,7]
# k = 3

nums = [-1,-100,3,99]
k = 2

nums = [1,2,3]
k = 2

s = Solution()
s.rotate(nums,k)