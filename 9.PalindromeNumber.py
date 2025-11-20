class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(str(x) == str(x)[::-1])
        return str(x) == str(x)[::-1]
    
s = Solution()
s.isPalindrome(121)

# Time Complexity: O(n)
# Space Complexity: O(n)

OR

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        original = x
        
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        
        return rev == original
    
s = Solution()
s.isPalindrome(121)

# Time Complexity: O(n)
# Space Complexity: O(1)