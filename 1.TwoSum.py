class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        if not nums:
            return 0
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return i, j

s = Solution()
print(s.twoSum([2,7,11,15], 9))

#Time Complexity: O(n^2)
#Space Complexity: O(1)