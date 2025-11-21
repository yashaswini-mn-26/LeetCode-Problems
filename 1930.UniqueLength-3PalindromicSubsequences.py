class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
                print(f"first[{ch}] = {i}")
            last[ch] = i
            print(f"last[{ch}] = {i}")
        print(first)
        print(last)

        ans = 0

        for ch in first:
            l = first[ch]
            r = last[ch]

            if r - l > 1:
                middle_chars = set(s[l+1:r])
                ans += len(middle_chars)

        return ans

s = Solution()
s.countPalindromicSubsequence("aabca")

# Time Complexity: O(n)
# Space Complexity: O(1)