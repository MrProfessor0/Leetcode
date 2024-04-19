def binary_search(arr:list[int], start:int, end:int, key:int) -> int:

    mid = int((start+end)/2)

    while(start <= end):
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid + 1
        if arr[mid] > key:
            end = mid - 1
        mid = int((start+end)/2)
    return -1

def get_pivot(arr:list[int])->int:
    start = 0
    end = len(arr)-1

    while(start < end):
        mid = (start+end)//2

        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
    
    # print("element: " + str(arr[start]))
    return start

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot_index = get_pivot(arr=nums)
        print("pivot_index: " + str(pivot_index))

        if target >= nums[pivot_index] and target <= nums[-1]:
            index = binary_search(arr=nums, start=pivot_index, end=len(nums)-1, key=target)
        else:
            index = binary_search(arr=nums, start=0, end=pivot_index-1, key=target)
        
        return index

s = Solution()

# print(s.search(nums = [3,4,5,6,1,2], target = 2))
print(s.search(nums = [1,2,3,4,5,6], target = 2))
