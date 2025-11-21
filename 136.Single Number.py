class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        return nums[-1]

s = Solution()
s.singleNumber([4,1,2,1,2])

# Time Complexity: O(nlogn)
# Space Complexity: O(1)