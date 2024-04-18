def first_occurunce(nums: list[int], target: int) -> list[int]:
    start = 0
    end = len(nums)-1
    ans = -1

    while(start<=end):
        mid = (start+end)//2
        if nums[mid] == target:
            ans = mid
            end = mid - 1
            # return first
        if nums[mid] > target:
            end = mid - 1
        if nums[mid] < target:
            start = mid + 1

    return ans

def last_occurunce(nums: list[int], target: int) -> list[int]:
    start = 0
    end = len(nums)-1
    ans = -1

    while(start<=end):
        mid = (start+end)//2
        if nums[mid] == target:
            ans = mid
            start = mid + 1
        if nums[mid] > target:
            end = mid - 1
        if nums[mid] < target:
            start = mid + 1

    return ans

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        occurence = []
        occurence.append(first_occurunce(nums,target))
        occurence.append(last_occurunce(nums,target))
        return occurence

                
if __name__ == '__main__':

    nums = [5,7,7,8,8,10]
    target = 90
    s = Solution()

    print(s.searchRange(nums=nums,target=target))