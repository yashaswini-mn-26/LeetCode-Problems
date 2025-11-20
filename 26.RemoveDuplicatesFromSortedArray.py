class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]: 
                print("i am printing11",nums[j], nums[i])
                i += 1
                print("i am printing22",i)
                nums[i] = nums[j] 
                print("i am printing33",nums[i], nums[j])
        
        return i + 1 
s = Solution()
print(s.removeDuplicates([1,1,2]))


#Time Complexity: O(n)
#Space Complexity: O(1)