class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean_s == clean_s[::-1]
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")

# Time Complexity: O(n)
# Space Complexity: O(n)

OR

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")        

# Time Complexity: O(n)
# Space Complexity: O(n)+O(1)
