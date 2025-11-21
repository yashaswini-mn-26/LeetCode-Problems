class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0 
        
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k

s = Solution()
print(s.removeElement([3,2,2,3], 3))

# Time Complexity: O(n)
# Space Complexity: O(1)