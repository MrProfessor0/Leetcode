class Solution:
    def binary_search(self, x: int):
        start = 0
        end = x
        ans = 0

        while(start<=end):
            mid = start + (end-start)//2
            square = mid * mid

            if square == x:
                return mid
            if square > x:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        
        return ans

    def mySqrt(self, x: int) -> int:
        print(self.binary_search(x))


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(x=10))