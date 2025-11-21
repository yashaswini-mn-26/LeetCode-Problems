class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total = 0

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                total += i
        
        return total == num

s = Solution()
s.checkPerfectNumber(28)

# Time Complexity: O(n)
# Space Complexity: O(1)