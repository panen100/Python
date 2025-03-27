class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if  nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

solution = Solution()                        
result = solution.searchInsert([1,3,5,6],2)
print(result)